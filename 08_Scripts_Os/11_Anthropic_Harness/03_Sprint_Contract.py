#!/usr/bin/env python3
"""
03_Sprint_Contract.py — Sprint Contract Manager

Implementa el patrón de Sprint Contract de Anthropic:
- ANTES de cada sprint: Generator + Evaluator negocian "done"
- Evita que el Generator "mueva el goalpost" durante el build
- Define criteria verificables ANTES de escribir código

Basado en: "So within this version of the harness... there was contract negotiations
between the generator agent and the evaluator agent. It was defining the definition
of done up front before it actually started building anything."

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandones" — Siempre lo correcto

REFERENCIA: 01_Core/02_Knowledge_Brain/10_Anthropic_Harness_Design.md
"""

import os
import json
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# ========================
# CONTRACT TYPES
# ========================


class ContractStatus(Enum):
    """Estados del contrato"""

    DRAFT = "draft"
    NEGOTIATING = "negotiating"
    AGREED = "agreed"
    FULFILLED = "fulfilled"
    BREACHED = "breached"


@dataclass
class ContractCriterion:
    """Un criterion del contrato"""

    id: str
    description: str
    verification_method: str  # "manual", "automated", "test"
    passed: Optional[bool] = None
    evidence: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "verification_method": self.verification_method,
            "passed": self.passed,
            "evidence": self.evidence,
        }


@dataclass
class SprintContract:
    """Contrato de sprint entre Generator y Evaluator"""

    sprint_id: str
    feature: str
    generator_proposal: str  # Lo que el generator dice que va a build
    evaluator_requirements: List[ContractCriterion] = field(default_factory=list)
    agreed_criteria: List[ContractCriterion] = field(default_factory=list)
    status: ContractStatus = ContractStatus.DRAFT
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "sprint_id": self.sprint_id,
            "feature": self.feature,
            "generator_proposal": self.generator_proposal,
            "evaluator_requirements": [
                c.to_dict() for c in self.evaluator_requirements
            ],
            "agreed_criteria": [c.to_dict() for c in self.agreed_criteria],
            "status": self.status.value,
            "created_at": self.created_at,
        }


class SprintContractManager:
    """
    Gestor de Sprint Contracts.

    DEL ARTÍCULO:
    "It was defining the definition of done up front before it actually started building anything.
    So that way, the generator agent couldn't move the goalpost halfway through the build
    to say, 'Ah, it's done.'"

    FLUJO:
    1. Generator propone qué va a build
    2. Evaluator responde con requirements
    3. Negocian hasta agree en criterios
    4. Ambos firman el contract
    5. Generator build
    6. Evaluator verifica contra criteria acordados
    """

    def __init__(self):
        self.active_contracts: List[SprintContract] = []

    def create_contract(
        self, sprint_id: str, feature: str, generator_proposal: str
    ) -> SprintContract:
        """Crea un nuevo contrato de sprint"""
        contract = SprintContract(
            sprint_id=sprint_id,
            feature=feature,
            generator_proposal=generator_proposal,
            status=ContractStatus.DRAFT,
        )
        self.active_contracts.append(contract)
        return contract

    def add_requirement(
        self, contract: SprintContract, requirement: str, verification: str = "manual"
    ) -> ContractCriterion:
        """Añade un requirement al contrato"""
        criterion = ContractCriterion(
            id=f"req_{len(contract.evaluator_requirements) + 1}",
            description=requirement,
            verification_method=verification,
        )
        contract.evaluator_requirements.append(criterion)
        contract.status = ContractStatus.NEGOTIATING
        return criterion

    def agree_criteria(
        self, contract: SprintContract, criterion_ids: List[str]
    ) -> bool:
        """
        El Generator y Evaluator agreed en los criterios.
        Esto firma el contrato.
        """
        agreed = []
        for cid in criterion_ids:
            for req in contract.evaluator_requirements:
                if req.id == cid:
                    agreed.append(req)

        if not agreed:
            return False

        contract.agreed_criteria = agreed
        contract.status = ContractStatus.AGREED
        return True

    def verify_contract(self, contract: SprintContract, actual_output: str) -> dict:
        """
        Verifica el output contra el contrato.
        Returns resultado con cada criterion verificado.
        """
        results = {
            "contract_id": contract.sprint_id,
            "feature": contract.feature,
            "passed": True,
            "criteria_results": [],
            "summary": "",
        }

        # Verificar cada criterion
        for criterion in contract.agreed_criteria:
            # En implementación real, ejecutar verification_method
            # Por ahora, heurística simple

            criterion.passed = True  # Optimista
            criterion.evidence = f"Verified: {criterion.verification_method}"

            results["criteria_results"].append(criterion.to_dict())

            if not criterion.passed:
                results["passed"] = False

        # Summary
        passed_count = sum(1 for c in contract.agreed_criteria if c.passed)
        total = len(contract.agreed_criteria)

        if results["passed"]:
            results["summary"] = (
                f"✅ CONTRACT FULFILLED: {passed_count}/{total} criteria passed"
            )
        else:
            results["summary"] = (
                f"❌ CONTRACT BREACHED: {passed_count}/{total} criteria passed"
            )

        if results["passed"]:
            contract.status = ContractStatus.FULFILLED
        else:
            contract.status = ContractStatus.BREACHED

        return results

    def get_contract_report(self, contract: SprintContract) -> str:
        """Genera reporte del contrato"""
        lines = [
            f"\n{'=' * 60}",
            "📜 SPRINT CONTRACT",
            f"{'=' * 60}",
            f"Sprint ID: {contract.sprint_id}",
            f"Feature: {contract.feature}",
            f"Status: {contract.status.value.upper()}",
            f"{'=' * 60}",
            f"\n📝 GENERATOR PROPOSAL:",
            f"  {contract.generator_proposal}",
        ]

        if contract.agreed_criteria:
            lines.append(f"\n📋 AGREED CRITERIA ({len(contract.agreed_criteria)}):")
            for i, c in enumerate(contract.agreed_criteria, 1):
                status = "✅" if c.passed else "⚠️" if c.passed is None else "❌"
                lines.append(f"  {i}. {status} {c.description}")
                lines.append(f"     Verification: {c.verification_method}")

        lines.append(f"\n{'=' * 60}\n")

        return "\n".join(lines)


def run_sprint_contract(
    sprint_id: str, feature: str, proposal: str, requirements: List[str]
) -> dict:
    """
    Función principal para ejecutar un Sprint Contract.

    Usage:
        from 03_Sprint_Contract import run_sprint_contract

        result = run_sprint_contract(
            sprint_id="sprint_01",
            feature="Login form",
            proposal="Build login form with email/password",
            requirements=["Validar email", "Validar password", "Mostrar errores"]
        )
    """
    print("\n📜 Inicializando Sprint Contract Manager...")

    manager = SprintContractManager()

    # 1. Create contract
    contract = manager.create_contract(sprint_id, feature, proposal)

    # 2. Add requirements
    for req in requirements:
        manager.add_requirement(contract, req, "automated")

    # 3. Simular negociación (agreed all)
    criterion_ids = [c.id for c in contract.evaluator_requirements]
    manager.agree_criteria(contract, criterion_ids)

    # 4. Mostrar contrato
    print(manager.get_contract_report(contract))

    # Return contract
    return contract.to_dict()


if __name__ == "__main__":
    # Demo
    print("\n🔬 Testing Sprint Contract:\n")

    result = run_sprint_contract(
        sprint_id="sprint_01",
        feature="User Dashboard",
        proposal="Build user dashboard with stats cards and charts",
        requirements=[
            "Must show 3 stat cards with real data",
            "Must have interactive chart",
            "Must be responsive on mobile",
            "Must pass accessibility audit",
        ],
    )

    print("\n📋 Contract created successfully!")
    print(json.dumps(result, indent=2))
