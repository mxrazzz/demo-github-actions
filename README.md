# DevOps End-to-End Project

A hands-on DevOps project demonstrating Infrastructure as Code, Configuration Management, Containerization, and CI/CD pipelines.

## 🎯 Project Overview

This project showcases a complete DevOps workflow:

- **Flask API** - Simple web application returning system information
- **Docker** - Containerized application for portability
- **Terraform** - Infrastructure as Code for reproducible deployments
- **Ansible** - Configuration management for server setup
- **GitHub Actions** - Automated CI/CD pipeline with testing

## 🏗️ Architecture

```
Developer pushes code → GitHub Actions triggers
  ↓
Run pytest tests
  ↓
Build Docker image
  ↓
Test container deployment
  ↓
(Production: Deploy to cloud)
```

## 📁 Project Structure

```
├── app/                    # Application code
│   ├── app.py             # Flask application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Container definition
├── terraform/             # Infrastructure as Code
│   ├── main.tf           # Main Terraform config
│   ├── variables.tf      # Variable definitions
│   └── outputs.tf        # Output values
├── ansible/               # Configuration management
│   ├── playbook.yml      # Ansible playbook
│   └── inventory.ini     # Host inventory
├── .github/workflows/     # CI/CD pipelines
│   └── deploy.yml        # GitHub Actions workflow
└── tests/                 # Automated tests
    └── test_app.py       # pytest test suite
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Docker Desktop
- Terraform
- Ansible (optional)

### Run Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mxrazzz/demo-github-actions.git
   cd demo-github-actions
   ```

2. **Run with Docker:**

   ```bash
   cd app
   docker build -t flask-app:v1 .
   docker run -d -p 5000:5000 flask-app:v1
   ```

   Visit: http://localhost:5000

3. **Run with Terraform:**

   ```bash
   cd terraform
   terraform init
   terraform plan
   terraform apply
   ```

4. **Run tests:**
   ```bash
   pip install -r app/requirements.txt pytest
   pytest tests/ -v
   ```

## 🧪 Testing

The project follows a test-driven approach:

- Unit tests verify API endpoints
- Integration tests check Docker container functionality
- CI pipeline blocks deployment if tests fail

## 🔄 CI/CD Pipeline

GitHub Actions automatically:

1. Runs pytest tests on every push
2. Builds Docker images with commit SHA tags
3. Validates container deployment
4. (Production: Deploys to cloud infrastructure)

## 📚 Key Concepts Demonstrated

- **Infrastructure as Code (IaC)**: Terraform manages infrastructure declaratively
- **Idempotency**: Re-running deployments produces consistent results
- **Configuration Management**: Ansible automates server setup
- **Containerization**: Docker ensures consistent environments
- **Continuous Integration**: Automated testing on every commit
- **Continuous Deployment**: Automated deployment pipeline

## 🎓 Learning Outcomes

This project demonstrates:

- Modern DevOps toolchain proficiency
- Test-driven development practices
- Infrastructure automation skills
- Understanding of CI/CD principles
- Best practices for production deployments

## 📝 Notes

This project uses local Docker for demonstration. In production:

- Terraform would provision EC2/cloud instances
- Ansible would configure remote servers
- CI/CD would deploy to staging/production environments
- Monitoring and logging would be integrated

## 🔗 Resources

- [Terraform Documentation](https://www.terraform.io/docs)
- [Ansible Documentation](https://docs.ansible.com/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Built for HMRC Junior DevOps Engineer Interview - November 2025**
