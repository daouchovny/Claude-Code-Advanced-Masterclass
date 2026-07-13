# Technical Architecture Diagram Template

Use this template to document system architecture before generating the diagram.

## System Overview

### Title
[System name, e.g., "E-Commerce Platform Architecture"]

### Subtitle (Optional)
[Brief description, e.g., "Microservices-based scalable platform"]

### Purpose
[What this system does and why it exists]

---

## Architecture Layers

Define the logical layers of your system:

| Layer | Description | Components |
|-------|-------------|------------|
| Presentation | User-facing interfaces | Web App, Mobile App |
| API | Service interfaces | API Gateway, GraphQL |
| Business Logic | Core services | Auth, Orders, Payments |
| Data | Storage and caching | PostgreSQL, Redis |
| Infrastructure | Supporting services | Message Queue, Logging |

---

## Components

### Frontend Layer
| Component | Type | Technology | Description |
|-----------|------|------------|-------------|
| Web App | Frontend | React | Main web interface |
| Mobile App | Frontend | React Native | iOS/Android apps |
| Admin Portal | Frontend | Vue.js | Internal tools |

### API Layer
| Component | Type | Technology | Description |
|-----------|------|------------|-------------|
| API Gateway | API | Kong | Request routing, rate limiting |
| GraphQL API | API | Apollo | Unified data access |

### Service Layer
| Component | Type | Technology | Description |
|-----------|------|------------|-------------|
| Auth Service | Service | Node.js | Authentication/authorization |
| User Service | Service | Python | User management |
| Order Service | Service | Go | Order processing |
| Payment Service | Service | Java | Payment processing |
| Notification Service | Service | Node.js | Email/push notifications |

### Data Layer
| Component | Type | Technology | Description |
|-----------|------|------------|-------------|
| PostgreSQL | Database | PostgreSQL | Primary data store |
| Redis | Database | Redis | Caching layer |
| Elasticsearch | Database | ES | Search functionality |
| S3 | External | AWS S3 | File storage |

---

## Connections

Define how components communicate:

```
Web App -> API Gateway
Mobile App -> API Gateway
API Gateway -> Auth Service
API Gateway -> User Service
API Gateway -> Order Service
Auth Service -> PostgreSQL
User Service -> PostgreSQL
Order Service -> PostgreSQL
Order Service -> Payment Service
Order Service -> Redis
Payment Service -> External Payment API
Notification Service -> Redis
```

---

## Command to Generate

```bash
python3 pm_diagram_gen.py architecture \
  --title "E-Commerce Platform" \
  --subtitle "Microservices Architecture" \
  --components "Web App,Mobile App,API Gateway,Auth Service,User Service,Order Service,Payment Service,PostgreSQL,Redis" \
  --connections "Web App->API Gateway,Mobile App->API Gateway,API Gateway->Auth Service,API Gateway->Order Service,Order Service->PostgreSQL,Order Service->Redis" \
  --layers "Frontend,API,Services,Data" \
  --theme corporate
```

---

## Component Type Keywords

The diagram auto-colors components based on keywords in their names:

| Type | Color | Keywords |
|------|-------|----------|
| Frontend | Teal | web, app, ui, frontend, client |
| API | Red | api, gateway, rest, graphql |
| Service | Green | service, worker, queue |
| Database | Purple | db, database, postgres, mongo, redis, cache |
| External | Orange | external, third, 3rd, integration |

---

## Best Practices

1. **Group related components**: Use layers to organize logically
2. **Show key connections**: Focus on primary data/request flows
3. **Use consistent naming**: Match your team's terminology
4. **Keep it readable**: Limit to 8-12 components per diagram
5. **Version control**: Include diagrams in your repo
6. **Update regularly**: Keep architecture docs in sync with code
