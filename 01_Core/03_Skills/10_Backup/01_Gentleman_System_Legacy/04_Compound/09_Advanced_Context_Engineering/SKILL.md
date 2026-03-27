---
name: advanced-context-engineering
description: Sophisticated code analysis and modification using advanced context engineering principles. Use when analyzing or modifying existing codebases (especially TypeScript/JavaScript), refactoring components while maintaining type safety, investigating bugs or architectural issues, adding features to established projects, reviewing code architecture and dependencies, or when the user requests "context-aware" or "architectural" code analysis. Applies signal-to-noise optimization, layered architecture architecture analysis, pattern fidelity detection, progressive disclosure, and functional purity principles.
---

# Advanced Context Engineering

This skill enables sophisticated code analysis using advanced context engineering principles: maintaining architectural integrity, minimizing cognitive overhead, and ensuring changes are precise, scoped, and aligned with existing patterns.

## Supplementary References

For deeper understanding of specific techniques, consult these references as needed:

- **references/layer-architecture.md**: Complete layer examples, impact analysis templates, and violation patterns
- **references/pattern-detection.md**: Multi-dimensional pattern detection workflows and real-world examples
- **references/node-purity.md**: Purity scoring system, side effect catalog, and refactoring techniques

These files provide extensive examples and templates that complement the core workflow below.

## Core Principles

### 1. Signal-to-Noise Optimization
Minimize context pollution by loading only essential files.

**Process:**
- Create explicit dependency map before proposing changes
- Load in order of criticality: interfaces → types → implementations → tests
- Ignore node_modules, build artifacts, external dependencies unless requested
- Use targeted `view` with line ranges when possible

**Example:**
```bash
view /path/to/project           # Directory structure
view /path/to/types.ts          # Types first
view /path/to/component.tsx     # Implementation if needed
```

### 2. Context Layering Architecture
Maintain mental model of system layers and contracts.

**Layers (bottom to top):**
1. Type Layer: `.d.ts` files, type definitions, interfaces
2. Contract Layer: Abstract classes, base interfaces, API contracts
3. Implementation Layer: Concrete components, functions, classes
4. Integration Layer: Modules composing implementations
5. Application Layer: Entry points, configuration

**Rules:**
- Verify type definitions before modifying implementations
- When changing contract, trace all dependent implementations
- Document layer violations explicitly
- Use contracts-first approach

### 3. Pattern Fidelity
Detect and replicate existing patterns rather than importing generic solutions.

**Detection checklist:**
- [ ] Naming convention (camelCase, PascalCase, kebab-case)
- [ ] Error handling (try-catch, Either, Result types)
- [ ] Dependency injection (constructor, props, hooks)
- [ ] File organization (co-location, separation by type)
- [ ] Testing patterns (unit, integration, mocks)
- [ ] State management (useState, Redux, Zustand, Jotai)
- [ ] Async handling (async/await, callbacks, promises)

**Process:**
1. Analyze 3-5 similar files before writing new code
2. Extract common patterns
3. Create pattern template
4. Flag deviations with justification

### 4. Progressive Disclosure
Break complex tasks into structured phases with explicit checkpoints.

**Phases:**

**Phase 1: Impact Analysis**
- Identify affected files
- Map dependency chains
- Assess risk (low/medium/high)
- Estimate scope (LOC, files)

**Phase 2: Type Definition**
- Define/update TypeScript interfaces
- Verify type compatibility
- Update `.d.ts` files if needed
- Run type checking

**Phase 3: Implementation**
- Write core logic
- Maintain functional purity
- Add inline documentation
- Handle edge cases

**Phase 4: Integration**
- Update dependent modules
- Add tests
- Verify no regressions
- Update documentation

### 5. Node Anatomy
Treat each file as a node with explicit inputs and outputs.

**Node components:**
- **Inputs**: imports, props, parameters, env vars
- **Processing**: logic, transformations, side effects
- **Outputs**: exports, returns, side effects (API, DOM, localStorage)

**Purity guidelines:**
- Minimize side effects in pure functions
- Isolate I/O operations into dedicated modules
- Use dependency injection for testability
- Make implicit dependencies explicit

## Standard Operating Procedure

### 1. Initial Assessment (30 sec)
- Read user request
- Identify greenfield vs brownfield
- Determine complexity (simple/medium/complex)

### 2. Context Acquisition (1-3 min)
- View project structure
- Load essential files (types first)
- Identify architectural patterns

### 3. Impact Analysis (if complex)
- Map affected files
- Identify breaking changes
- Calculate refactoring scope

### 4. Type-First Development
- Define/update types and interfaces
- Verify type safety
- Document contracts

### 5. Implementation
- Follow detected patterns
- Maintain node purity
- Add error handling

### 6. Validation
- Verify no layer violations
- Check for unintended side effects
- Confirm pattern adherence

## Advanced Techniques

### Dependency Mapping
Create ASCII dependency graph before changes:

```
UserService
    ├─> UserRepository (interface)
    │       ├─> DatabaseUserRepository (impl)
    │       └─> MockUserRepository (impl)
    ├─> Logger (interface)
    └─> CacheService (interface)

IMPACT: Changing UserRepository affects 2 implementations
```

### Pattern Extraction Template

```markdown
## Detected Pattern: [Pattern Name]

**Location**: src/services/*.ts
**Frequency**: 8/10 files
**Pattern**:
- Key characteristic 1
- Key characteristic 2
- Key characteristic 3

**Template**:
[Code example showing pattern]
```

### Node Purity Score

```
File: src/utils/helpers.ts
Purity Score: 9/10
- ✅ Pure functions: 8/9
- ✅ No global state access
- ✅ All dependencies injected
- ⚠️ One function uses Date.now() (acceptable)
```

## Anti-Patterns to Avoid

1. **Context Overload**: Loading entire directories when 2-3 files suffice
2. **Pattern Ignorance**: Using external patterns without checking existing code
3. **Premature Generalization**: Adding abstractions before patterns clear
4. **Layer Violations**: Implementation details leaking into type definitions
5. **Hidden Dependencies**: Undocumented global state or singletons
6. **Shotgun Surgery**: Small changes across many files vs refactoring

## Quality Checklist

Before delivering:

- [ ] Only essential files loaded
- [ ] Types defined before implementations
- [ ] Existing patterns replicated
- [ ] Node purity maintained (side effects isolated)
- [ ] Layer boundaries respected
- [ ] Breaking changes documented
- [ ] Tests added for new logic
- [ ] No generic solutions without validation

## Output Format

### For Simple Tasks
Direct implementation with brief explanation.

### For Complex Tasks
Use this structure:

```markdown
## Phase 1: Impact Analysis
Files affected:
- [file path] ([action]: ADD/MODIFY/DELETE)
- [file path] (READ ONLY)

Risk Level: [LOW/MEDIUM/HIGH]
Scope: ~[number] lines, [number] files

## Phase 2: Type Definitions
[Show type changes]

Type safety: ✅/⚠️ [explanation]

## Phase 3: Implementation
Detected pattern: [pattern description]

[Implementation code]

## Phase 4: Integration
[Integration steps if needed]
```

## Refactoring Workflow

When refactoring:

1. **Extract Current Architecture**
   ```
   Current: [Current approach]
   Target: [Desired approach]
   Migration Path: [Step by step]
   ```

2. **Create Migration Plan**
   - Phase 1: [No breaking changes]
   - Phase 2: [Gradual migration]
   - Phase 3: [Complete transition]
   - Phase 4: [Cleanup]

3. **Execute with Checkpoints**
   - Verify tests after each phase
   - No breaking changes per phase
   - Each phase independently deployable

## Debugging Workflow

1. Identify problematic node (file/function)
2. Analyze inputs: Expected?
3. Analyze processing: Impure operations?
4. Analyze outputs: Match contract?
5. Trace upstream: Input sources?
6. Trace downstream: Output consumers?

## Key Takeaways

This skill ensures:
- **Precision**: Only necessary files touched
- **Safety**: Types verified before implementation
- **Consistency**: Patterns detected and replicated
- **Maintainability**: Node purity and layer separation preserved
- **Traceability**: Impact explicitly mapped before changes
