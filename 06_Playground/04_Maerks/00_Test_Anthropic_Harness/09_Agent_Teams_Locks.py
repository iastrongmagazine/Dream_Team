"""
Agent Teams con Git Locks - Sistema de coordinación para múltiples agentes

Inspirado en: "Scaling Agentic Systems" article (Feb 25, 2026)
Permite que múltiples agentes trabajen en paralelo sin pisarse.
"""

import os
import json
import time
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import threading


class LockState(Enum):
    """Estados posibles de un lock."""

    FREE = "FREE"
    LOCKED = "LOCKED"
    RELEASED = "RELEASED"
    EXPIRED = "EXPIRED"


@dataclass
class TaskLock:
    """Representa un lock en una tarea."""

    task_name: str
    agent_id: str
    state: LockState
    acquired_at: str = field(default_factory=lambda: datetime.now().isoformat())
    expires_at: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def is_valid(self) -> bool:
        """Check si el lock sigue válido para nuevas adquisiciones."""
        if self.state != LockState.LOCKED:
            return False
        if self.expires_at:
            expiry = datetime.fromisoformat(self.expires_at)
            if datetime.now() > expiry:
                return False
        return True

    def to_dict(self) -> Dict:
        return {
            "task_name": self.task_name,
            "agent_id": self.agent_id,
            "state": self.state.value,
            "acquired_at": self.acquired_at,
            "expires_at": self.expires_at,
            "metadata": self.metadata,
        }


class GitLockManager:
    """
    Manager de locks basado en archivos (como Git locks).

    Usa archivos de lock en un directorio para coordinar agentes.
    """

    def __init__(self, lock_dir: str = "current_tasks", ttl_seconds: int = 3600):
        """
        Args:
            lock_dir: Directorio donde se crean los archivos de lock
            ttl_seconds: Tiempo de vida máximo de un lock (default 1 hora)
        """
        self.lock_dir = lock_dir
        self.ttl_seconds = ttl_seconds
        self._locks: Dict[str, TaskLock] = {}
        self._lock = threading.Lock()

        # Crear directorio de locks si no existe
        os.makedirs(lock_dir, exist_ok=True)

    def _get_lock_path(self, task_name: str) -> str:
        """Obtiene la ruta del archivo de lock."""
        safe_name = task_name.replace("/", "_").replace("\\", "_")
        return os.path.join(self.lock_dir, f"{safe_name}.lock")

    def acquire_lock(
        self,
        task_name: str,
        agent_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
    ) -> TaskLock:
        """
        Intenta adquirir un lock en una tarea.

        Args:
            task_name: Nombre de la tarea
            agent_id: ID del agente que quiere el lock (auto-generado si no se pasa)
            metadata: Metadata adicional

        Returns:
            TaskLock con la información del lock adquirido

        Raises:
            RuntimeError si el lock ya está tomado
        """
        with self._lock:
            lock_path = self._get_lock_path(task_name)
            agent_id = agent_id or f"agent-{uuid.uuid4().hex[:8]}"
            metadata = metadata or {}

            # Check si ya existe un lock válido
            if os.path.exists(lock_path):
                with open(lock_path, "r") as f:
                    existing = json.load(f)

                existing_lock = TaskLock(
                    task_name=existing["task_name"],
                    agent_id=existing["agent_id"],
                    state=LockState(existing["state"]),
                    acquired_at=existing["acquired_at"],
                    expires_at=existing.get("expires_at"),
                    metadata=existing.get("metadata", {}),
                )

                if existing_lock.is_valid():
                    raise RuntimeError(f"Lock already held by {existing_lock.agent_id}")

            # Crear nuevo lock
            expires_at = datetime.now().timestamp() + self.ttl_seconds
            lock = TaskLock(
                task_name=task_name,
                agent_id=agent_id,
                state=LockState.LOCKED,
                expires_at=datetime.fromtimestamp(expires_at).isoformat(),
                metadata=metadata,
            )

            # Escribir archivo de lock
            with open(lock_path, "w") as f:
                json.dump(lock.to_dict(), f, indent=2)

            self._locks[task_name] = lock
            return lock

    def release_lock(self, task_name: str, agent_id: Optional[str] = None) -> bool:
        """
        Libera un lock.

        Args:
            task_name: Nombre de la tarea
            agent_id: ID del agente que libera (debe ser el mismo que lo adquirió)

        Returns:
            True si se liberó correctamente, False si no había lock o no coincidía el agent_id
        """
        with self._lock:
            lock_path = self._get_lock_path(task_name)

            if not os.path.exists(lock_path):
                return False

            with open(lock_path, "r") as f:
                existing = json.load(f)

            # Verificar que el agente que libera es el mismo que lo adquirió
            if agent_id and existing["agent_id"] != agent_id:
                return False

            # Actualizar estado
            existing["state"] = LockState.RELEASED.value
            existing["released_at"] = datetime.now().isoformat()

            with open(lock_path, "w") as f:
                json.dump(existing, f, indent=2)

            if task_name in self._locks:
                self._locks[task_name].state = LockState.RELEASED

            return True

    def get_lock_status(self, task_name: str) -> Optional[TaskLock]:
        """Obtiene el estado de un lock."""
        with self._lock:
            lock_path = self._get_lock_path(task_name)

            if not os.path.exists(lock_path):
                return None

            with open(lock_path, "r") as f:
                data = json.load(f)

            # Parsear estado directamente del JSON, no inferirlo
            lock = TaskLock(
                task_name=data["task_name"],
                agent_id=data["agent_id"],
                state=LockState(data["state"]),
                acquired_at=data["acquired_at"],
                expires_at=data.get("expires_at"),
                metadata=data.get("metadata", {}),
            )

            return lock

    def list_all_locks(self) -> List[TaskLock]:
        """Lista todos los locks activos."""
        locks = []

        with self._lock:
            if not os.path.exists(self.lock_dir):
                return []

            for filename in os.listdir(self.lock_dir):
                if filename.endswith(".lock"):
                    filepath = os.path.join(self.lock_dir, filename)
                    with open(filepath, "r") as f:
                        data = json.load(f)

                    # Parsear estado directamente del JSON
                    lock = TaskLock(
                        task_name=data["task_name"],
                        agent_id=data["agent_id"],
                        state=LockState(data["state"]),
                        acquired_at=data["acquired_at"],
                        expires_at=data.get("expires_at"),
                        metadata=data.get("metadata", {}),
                    )
                    locks.append(lock)

        return locks

    def cleanup_expired(self) -> int:
        """Limpia locks expirados (solo los que están LOCKED y expirados)."""
        cleaned = 0

        with self._lock:
            if not os.path.exists(self.lock_dir):
                return 0

            for filename in os.listdir(self.lock_dir):
                if filename.endswith(".lock"):
                    filepath = os.path.join(self.lock_dir, filename)
                    with open(filepath, "r") as f:
                        data = json.load(f)

                    # Solo limpiar si está en estado LOCKED y expiró
                    if data.get("state") == LockState.LOCKED.value:
                        expires_at = data.get("expires_at")
                        if expires_at:
                            expiry = datetime.fromisoformat(expires_at)
                            if datetime.now() > expiry:
                                os.remove(filepath)
                                cleaned += 1

        return cleaned


class AgentTeam:
    """
    Equipo de agentes que trabajan en paralelo con locks.
    """

    def __init__(
        self,
        name: str,
        num_agents: int = 4,
        lock_manager: Optional[GitLockManager] = None,
    ):
        self.name = name
        self.num_agents = num_agents
        self.lock_manager = lock_manager or GitLockManager()
        self.agents: Dict[str, Dict[str, Any]] = {}
        self.task_queue: List[str] = []
        self.completed_tasks: List[str] = []

    def register_agent(self, agent_id: str, role: str = "worker") -> None:
        """Registra un agente en el equipo."""
        self.agents[agent_id] = {
            "role": role,
            "status": "idle",
            "current_task": None,
            "joined_at": datetime.now().isoformat(),
        }

    def add_task(self, task_name: str, priority: int = 0) -> None:
        """Agrega una tarea a la cola."""
        # Insertar según prioridad
        inserted = False
        for i, t in enumerate(self.task_queue):
            if priority > self._get_task_priority(t):
                self.task_queue.insert(i, task_name)
                inserted = True
                break
        if not inserted:
            self.task_queue.append(task_name)

    def _get_task_priority(self, task_name: str) -> int:
        """Obtiene la prioridad de una tarea (para ordenamiento)."""
        # Por defecto todas tienen prioridad 0
        return 0

    def assign_next_task(self, agent_id: str) -> Optional[str]:
        """
        Asigna la siguiente tarea disponible a un agente.

        Returns:
            Nombre de la tarea asignada, o None si no hay tareas
        """
        if agent_id not in self.agents:
            return None

        # Buscar primera tarea sin lock
        for task_name in self.task_queue:
            if task_name in self.completed_tasks:
                continue

            status = self.lock_manager.get_lock_status(task_name)
            if status is None or status.state == LockState.FREE:
                try:
                    lock = self.lock_manager.acquire_lock(task_name, agent_id)
                    self.agents[agent_id]["current_task"] = task_name
                    self.agents[agent_id]["status"] = "working"
                    return task_name
                except RuntimeError:
                    # Ya tiene lock otro agente, continuar
                    continue

        return None

    def complete_task(self, agent_id: str, task_name: str) -> bool:
        """Marca una tarea como completada."""
        if agent_id not in self.agents:
            return False

        if self.agents[agent_id].get("current_task") != task_name:
            return False

        # Liberar lock
        self.lock_manager.release_lock(task_name, agent_id)

        # Actualizar estado del agente
        self.agents[agent_id]["current_task"] = None
        self.agents[agent_id]["status"] = "idle"

        # Marcar tarea como completada
        if task_name not in self.completed_tasks:
            self.completed_tasks.append(task_name)

        return True

    def get_team_status(self) -> Dict[str, Any]:
        """Obtiene el estado del equipo."""
        working = sum(1 for a in self.agents.values() if a["status"] == "working")
        idle = sum(1 for a in self.agents.values() if a["status"] == "idle")

        return {
            "team_name": self.name,
            "total_agents": len(self.agents),
            "working": working,
            "idle": idle,
            "pending_tasks": len(self.task_queue) - len(self.completed_tasks),
            "completed_tasks": len(self.completed_tasks),
            "agents": self.agents,
        }


# ==================== TESTS ====================


def test_lock_acquire_release():
    """Test acquire y release de locks."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        manager = GitLockManager(lock_dir=os.path.join(tmpdir, "locks"))

        # Acquire lock
        lock = manager.acquire_lock("task-1", "agent-1")
        assert lock.state == LockState.LOCKED
        assert lock.agent_id == "agent-1"

        # Check que existe archivo
        assert os.path.exists(manager._get_lock_path("task-1"))

        # Release lock
        result = manager.release_lock("task-1", "agent-1")
        assert result == True, f"Release failed, result={result}"

        # Verify lock liberado
        status = manager.get_lock_status("task-1")
        print(
            f"DEBUG: status.state={status.state}, status.state.value={status.state.value if status else 'N/A'}"
        )
        assert status.state == LockState.RELEASED, (
            f"Expected RELEASED, got {status.state}"
        )


def test_lock_conflict():
    """Test que dos agentes no pueden tomar el mismo lock."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        manager = GitLockManager(lock_dir=os.path.join(tmpdir, "locks"))

        # Agent 1 toma el lock
        lock1 = manager.acquire_lock("task-1", "agent-1")
        assert lock1.agent_id == "agent-1"

        # Agent 2 intenta y falla
        try:
            manager.acquire_lock("task-1", "agent-2")
            assert False, "Should have raised exception"
        except RuntimeError as e:
            assert "already held" in str(e)


def test_team_status():
    """Test estado del equipo."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        manager = GitLockManager(lock_dir=os.path.join(tmpdir, "locks"))
        team = AgentTeam("test-team", num_agents=3, lock_manager=manager)

        # Registrar agentes
        team.register_agent("agent-1", "worker")
        team.register_agent("agent-2", "worker")
        team.register_agent("agent-3", "worker")

        # Agregar tareas
        team.add_task("task-1")
        team.add_task("task-2")

        # Asignar tareas
        task1 = team.assign_next_task("agent-1")
        task2 = team.assign_next_task("agent-2")

        assert task1 == "task-1"
        assert task2 == "task-2"

        # Completar tareas
        team.complete_task("agent-1", "task-1")
        team.complete_task("agent-2", "task-2")

        # Check status after completion
        # All agents are now idle (they finished their work)
        status = team.get_team_status()
        assert status["completed_tasks"] == 2
        assert status["working"] == 0  # All done, all idle
        assert status["idle"] == 3  # All 3 agents idle


def test_cleanup_expired():
    """Test limpieza de locks expirados."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        manager = GitLockManager(lock_dir=os.path.join(tmpdir, "locks"), ttl_seconds=1)

        # Tomar un lock (expira en 1 segundo)
        manager.acquire_lock("task-1", "agent-1")

        # Esperar a que expire
        import time

        time.sleep(1.1)

        # Cleanup
        cleaned = manager.cleanup_expired()
        assert cleaned >= 1, f"Expected at least 1 expired lock, got {cleaned}"


if __name__ == "__main__":
    print("=" * 60)
    print("Agent Teams with Git Locks - Tests")
    print("=" * 60)

    test_lock_acquire_release()
    print("[PASS] test_lock_acquire_release")

    test_lock_conflict()
    print("[PASS] test_lock_conflict")

    test_team_status()
    print("[PASS] test_team_status")

    test_cleanup_expired()
    print("[PASS] test_cleanup_expired")

    print()
    print("*** ALL TESTS PASSED ***")
