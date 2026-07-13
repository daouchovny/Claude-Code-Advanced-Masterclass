---
name: pm-diagrams
triggers:
  - user journey
  - user flow
  - journey map
  - customer journey
  - architecture diagram
  - system architecture
  - technical architecture
  - flow diagram
  - process flow
  - sequence diagram
  - component diagram
  - generate diagram
  - create diagram
  - pm diagram
  - product diagram
---

# PM Diagrams Skill

You are helping product managers create professional visual diagrams. This skill generates two main types of diagrams:

1. **User Journey Maps** - Visualize the customer experience across touchpoints
2. **Technical Architecture Diagrams** - Document system components and their relationships

## How to Use

When the user requests a diagram, follow these steps:

### Step 1: Identify Diagram Type

Ask the user (if not clear) which type they need:
- **User Journey**: For customer flows, onboarding, feature adoption paths
- **Architecture**: For system design, service interactions, data flow

### Step 2: Gather Requirements

For **User Journey Maps**, collect:
- Persona name and description
- Journey stages (e.g., Awareness, Consideration, Purchase, Retention)
- Touchpoints at each stage
- User emotions/pain points (optional)
- Actions and goals

For **Architecture Diagrams**, collect:
- System components (services, databases, APIs)
- Component relationships and data flow
- External integrations
- Technology stack (optional)

### Step 3: Generate the Diagram

Use the diagram generator script located at `pm_diagram_gen.py` in the project root.

```bash
# For User Journey
python3 pm_diagram_gen.py journey --title "User Onboarding Journey" --stages "Discover,Sign Up,Onboard,Activate,Engage"

# For Architecture
python3 pm_diagram_gen.py architecture --title "E-Commerce Platform" --components "Web App,API Gateway,Auth Service,Product Service,Payment Service,Database"
```

### Step 4: Customize as Needed

The script supports these customization options:
- `--title`: Diagram title
- `--subtitle`: Secondary description
- `--output`: Custom output filename
- `--theme`: Color theme (default, dark, light, corporate)

## Example Templates

Reference these for structure and content:
- `examples/user-journey-template.md` - User journey structure
- `examples/architecture-template.md` - Architecture components
- `examples/sample-journeys.md` - Real-world journey examples

## Output

Diagrams are saved as PNG files in the current directory with timestamps for versioning.

## Tips for PMs

1. **Keep it simple**: Start with 4-6 stages/components, expand if needed
2. **Focus on key touchpoints**: Not every interaction needs to be mapped
3. **Use consistent naming**: Match your team's terminology
4. **Include pain points**: They drive product decisions
5. **Version your diagrams**: Use timestamps or git for tracking changes
