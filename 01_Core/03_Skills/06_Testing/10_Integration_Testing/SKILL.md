---
name: integration-testing-skill
description: > Triggers on: testing, QA, quality, validation.
  Integration testing patterns for multi-component systems. Includes API testing, database testing, and service mocking.
  Trigger: integration testing, API integration, service mocking, database testing, contract testing, component testing.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# Integration Testing Skill — Multi-Component Testing

## When to Use

- Testing component interactions
- API integration testing
- Database integration testing
- Service mocking and stubbing
- Contract testing between services
- End-to-end integration flows

## Critical Patterns

### 1. Integration Test Pyramid

```
┌─────────────────────────────────────────────────────────────────┐
│                  INTEGRATION TEST LAYERS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                    ┌─────────────────┐                          │
│                    │   API GATEWAY   │  ← External APIs       │
│                    └────────┬────────┘                          │
│                             │                                    │
│              ┌─────────────┴─────────────┐                      │
│              │      SERVICE LAYER       │                      │
│              │   (Business Logic)        │                      │
│              └─────────────┬─────────────┘                      │
│                            │                                    │
│         ┌──────────────────┼──────────────────┐                  │
│         │         DATA ACCESS LAYER          │                  │
│         │    (Database, Cache, Storage)       │                  │
│         └────────────────────────────────────┘                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Test Containers Pattern

```python
import pytest
import testcontainers
from testcontainers.postgres import PostgresContainer
from testcontainers.redis import RedisContainer

@pytest.fixture(scope="module")
def postgres():
    """Real PostgreSQL in Docker for integration tests."""
    with PostgresContainer("postgres:15-alpine") as postgres:
        yield postgres

@pytest.fixture(scope="module")
def redis():
    """Real Redis in Docker for integration tests."""
    with RedisContainer("redis:7-alpine") as redis:
        yield redis

@pytest.fixture(scope="module")
def db_connection(postgres):
    """Database connection with real PostgreSQL."""
    from sqlalchemy import create_engine
    engine = create_engine(postgres.get_connection_url())
    yield engine
    engine.dispose()
```

### 3. Service Mocking with Responses

```python
import responses
from requests import get

@responses.activate
def test_external_api_mock():
    """Mock external API without hitting network."""
    responses.add(
        responses.GET,
        "https://api.example.com/users/123",
        json={"id": 123, "name": "Test User"},
        status=200
    )
    
    response = get("https://api.example.com/users/123")
    
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

@responses.activate
def test_api_error_handling():
    """Test API error handling with mocked 500."""
    responses.add(
        responses.GET,
        "https://api.example.com/users/123",
        json={"error": "Internal Error"},
        status=500
    )
    
    with pytest.raises(APIError) as exc_info:
        fetch_user(123)
    
    assert exc_info.value.status_code == 500
```

## Code Examples

### API Integration Tests

```python
import pytest
from httpx import AsyncClient, ASGITransport
from app import app

@pytest.mark.asyncio
async def test_create_user_integration():
    """Full stack test with real database."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        # Create user
        response = await client.post(
            "/api/users",
            json={"email": "test@example.com", "name": "Test User"}
        )
        assert response.status_code == 201
        user_id = response.json()["id"]
        
        # Retrieve user
        response = await client.get(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["email"] == "test@example.com"
        
        # Verify in database
        user = await db.users.get(user_id)
        assert user.email == "test@example.com"
```

### Contract Testing (Pact)

```python
# Consumer side
import pytest
from pact import Consumer, Provider

@pytest.fixture
def pact():
    consumer = Consumer("UserService")
    provider = Provider("UserAPI")
    return consumer, provider

def test_user_contract(pact):
    consumer, provider = pact
    
    (consumer
     .having_interaction(
         "GET user by ID",
         provider_state="user 123 exists"
     )
     .upon_receiving("a request for user 123")
     .with_request("GET", "/users/123")
     .with_query(params={"include": "profile"})
     .will_respond_with(200)
     .with_content({
         "id": 123,
         "name": "Test User",
         "email": "test@example.com"
     })
     .with_headers({"Content-Type": "application/json"})
     .write_to_pact("./pacts/user-consumer-user-api.json"))
```

### Database Integration Tests

```python
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

@pytest.fixture
async def db_engine():
    """Create test database with migrations."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    await engine.dispose()

@pytest.fixture
async def db_session(db_engine):
    """Async session for tests."""
    async_session = async_sessionmaker(db_engine, expire_on_commit=False)
    
    async with async_session() as session:
        yield session
        await session.rollback()

@pytest.mark.asyncio
async def test_user_repository_crud(db_session):
    """Test UserRepository with real database."""
    from app.repositories import UserRepository
    
    repo = UserRepository(db_session)
    
    # Create
    user = await repo.create(User(name="Test", email="test@example.com"))
    assert user.id is not None
    
    # Read
    retrieved = await repo.get(user.id)
    assert retrieved.name == "Test"
    
    # Update
    retrieved.name = "Updated"
    await repo.update(retrieved)
    
    # Delete
    await repo.delete(user.id)
    assert await repo.get(user.id) is None
```

## Commands

```bash
# Run integration tests with Docker
pytest tests/integration/ --use-docker

# Start test containers
docker-compose -f docker-compose.test.yml up -d

# Run with database
pytest tests/integration/db/ --postgres-url=postgresql://localhost/test

# Contract testing
pact-broker publish ./pacts --provider-version=1.0.0
pact-broker can-i-deploy --pacticipant=UserService

# Run all integration tests
pytest tests/integration/ -v --tb=short
```

## Resources

- **TestContainers**: https://testcontainers.com/
- **Pact**: https://docs.pact.io/
- **pytest-asyncio**: https://pytest-asyncio.readthedocs.io/
- **responses**: https://github.com/getsentry/responses
- **HTTPCraft**: https://github.com/kaivi/httpx-mock

## Esencia Original
> **Propósito:** 10_Integration_Testing - propósito del skill
> **Flujo:** Pasos principales del flujo de trabajo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 📁 Progressive Disclosure

> Para información detallada:
- [references/guide.md](references/guide.md) — Guía completa

## 🛠️ Scripts

- [scripts/run.py](scripts/run.py) — Script principal

## 💾 State Persistence

Guardar en:
-  — Evaluaciones
-  — Documentación

