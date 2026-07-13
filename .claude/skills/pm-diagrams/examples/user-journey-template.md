# User Journey Map Template

Use this template to structure user journey information before generating the diagram.

## Journey Details

### Title
[Name of the journey, e.g., "New User Onboarding Journey"]

### Subtitle (Optional)
[Brief description, e.g., "From first visit to active user"]

### Persona
- **Name**: [User persona name]
- **Role**: [Job title or user type]
- **Goals**: [What they want to achieve]
- **Pain Points**: [Current frustrations]

---

## Journey Stages

Define 4-6 stages that represent the key phases of the user's experience.

| Stage | Description |
|-------|-------------|
| 1. Awareness | User discovers the product |
| 2. Consideration | User evaluates if it meets their needs |
| 3. Sign Up | User creates an account |
| 4. Onboarding | User learns the basics |
| 5. Activation | User experiences core value |
| 6. Engagement | User becomes a regular user |

---

## Stage Details

### Stage 1: [Name]
- **Touchpoints**: [Where/how user interacts - website, email, ad, etc.]
- **Actions**: [What the user does]
- **Emotions**: [How they feel - excited, confused, frustrated, etc.]
- **Opportunities**: [How we can improve this stage]

### Stage 2: [Name]
- **Touchpoints**:
- **Actions**:
- **Emotions**:
- **Opportunities**:

[Repeat for all stages]

---

## Command to Generate

```bash
python3 pm_diagram_gen.py journey \
  --title "New User Onboarding Journey" \
  --subtitle "From first visit to active user" \
  --stages "Awareness,Consideration,Sign Up,Onboarding,Activation" \
  --touchpoints "Ads/Social,Website/Reviews,Sign Up Form,Welcome Email,Core Feature" \
  --emotions "Curious,Evaluating,Hopeful,Learning,Delighted" \
  --actions "Clicks ad,Browses features,Creates account,Follows tutorial,Completes first task" \
  --theme default
```

---

## Best Practices

1. **Keep stages focused**: Each stage should represent a distinct phase
2. **Be specific with touchpoints**: Name the actual channels/interfaces
3. **Capture real emotions**: Use research data, not assumptions
4. **Identify opportunities**: Note where improvements can be made
5. **Validate with users**: Test your journey map against real user feedback
