# Hybrid Deployment Lab: AWS + On-Prem Linux

One pipeline deploys the same app to an AWS EC2 server and an on-prem style Linux server, with hardening and SSL.

## What it does
- **Terraform**: provisions the AWS EC2 instance, key pair and security group (SSH restricted to one IP, encrypted root volume)
- **Ansible**: one idempotent playbook configures both servers (Nginx reverse proxy, systemd service, UFW firewall, fail2ban, SSH hardening)
- **GitHub Actions**: push to main deploys to AWS, runs a health check, then deploys on-prem and health-checks again
- **SSL**: Let's Encrypt certificate with auto-renewal on the on-prem server (DNS-01 challenge)

## Architecture
Developer push -> GitHub Actions (self-hosted runner) -> Ansible -> AWS EC2 + on-prem Linux server

## Security notes
- SSH key-only login, root login disabled, max 3 auth attempts
- Firewall allows only SSH, 80, 443
- AWS security group allows SSH from a single IP
- Secrets are never committed

## Run it
    ansible-playbook -i inventory.ini site.yml --limit aws
    ansible-playbook -i inventory.ini site.yml --limit onprem
