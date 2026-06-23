#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from main.models import Profile, Skill, Project, Experience, Education
import os

if not Profile.objects.exists():
    Profile.objects.create(
        name='Vishal Yadav',
        title='Full Stack Developer | AI & Django Expert',
        bio='Computer Science undergraduate with experience in Full Stack Development, Software Engineering, Backend Development, Mobile Application Development, and AI-powered applications. Skilled in building scalable web, desktop, and mobile apps using Python, Django, React.js, Flutter, SQL Server, and REST APIs. Experienced in AI integration, Agentic AI workflows, and cloud-ready architectures. Solved 999+ Data Structures and Algorithms problems.',
        email='vishalyaduvansi8081@gmail.com',
        phone='+91-9648169281',
        location='Kanpur, Uttar Pradesh, India',
        github='https://github.com/Vishal-9648169281',
        linkedin='https://www.linkedin.com/in/vishalyadavdev/',
        years_experience=1,
        projects_completed=10,
        happy_clients=999,
    )

if not Skill.objects.exists():
    skills = [
        ('React.js', 85, 'frontend', 'fab fa-react', 1),
        ('JavaScript', 88, 'frontend', 'fab fa-js', 2),
        ('TypeScript', 80, 'frontend', 'fas fa-code', 3),
        ('HTML5 / CSS3', 92, 'frontend', 'fab fa-html5', 4),
        ('Tailwind CSS', 82, 'frontend', 'fas fa-paint-brush', 5),
        ('Bootstrap', 88, 'frontend', 'fab fa-bootstrap', 6),
        ('Python', 92, 'backend', 'fab fa-python', 1),
        ('Django', 90, 'backend', 'fas fa-server', 2),
        ('Django REST Framework', 88, 'backend', 'fas fa-code', 3),
        ('FastAPI', 78, 'backend', 'fas fa-bolt', 4),
        ('Node.js / Express.js', 75, 'backend', 'fab fa-node-js', 5),
        ('Flutter', 78, 'backend', 'fas fa-mobile-alt', 6),
        ('SQL Server', 85, 'database', 'fas fa-database', 1),
        ('MySQL', 85, 'database', 'fas fa-database', 2),
        ('SQLite', 90, 'database', 'fas fa-database', 3),
        ('MongoDB', 78, 'database', 'fas fa-leaf', 4),
        ('Git & GitHub', 90, 'tools', 'fab fa-git-alt', 1),
        ('Docker', 72, 'tools', 'fab fa-docker', 2),
        ('Linux', 80, 'tools', 'fab fa-linux', 3),
        ('Machine Learning / NLP', 78, 'tools', 'fas fa-brain', 4),
        ('LangChain / Agentic AI', 75, 'tools', 'fas fa-robot', 5),
        ('LLM / RAG / Prompt Eng.', 74, 'tools', 'fas fa-microchip', 6),
    ]
    for name, pct, cat, icon, order in skills:
        Skill.objects.create(name=name, percentage=pct, category=cat, icon=icon, order=order)

if not Project.objects.exists():
    projects = [
        ('SmartBuy360', 'AI-Powered E-Commerce Price Comparison Platform. Designed scalable architecture for price comparison and recommendation systems. Built backend workflows using Node.js, Express.js, and MongoDB. Planned AI-powered image search and barcode-based product discovery.', 'Node.js, Express.js, MongoDB, AI/ML, REST APIs', True, 1),
        ('AI-Based IT Support Ticket Auto-Triage', 'Intelligent ticket routing using transformer-based NLP models. Automated issue classification and response generation. Integrated ML inference with Django backend workflows for seamless support automation.', 'Python, Django, NLP, Transformers, Machine Learning', True, 2),
        ('Full Stack Enterprise Applications', 'Developing enterprise software solutions and custom applications for clients across multiple industries at CTC Chandigarh. Building scalable architectures with Python, Django, React.js, and SQL Server.', 'Python, Django, React.js, SQL Server, REST APIs', False, 3),
        ('Cloud-Ready Mobile Applications', 'Designing and modernizing desktop, web, Android and iOS applications. Building scalable software architectures and cloud-ready systems using Flutter for cross-platform mobile development.', 'Flutter, Dart, Android, iOS, Firebase', False, 4),
    ]
    for title, desc, tech, featured, order in projects:
        Project.objects.create(title=title, description=desc, tech_stack=tech, featured=featured, order=order)

if not Experience.objects.exists():
    Experience.objects.create(
        role='Software Developer',
        company='CTC Solutions (Chandigarh Team Computers), Chandigarh',
        duration='Jun 2026 - Present',
        description='Developing enterprise software solutions and custom applications for clients across multiple industries. Working on Full Stack Development using Python, Django, React.js, JavaScript, SQL Server, and REST APIs. Designing and modernizing desktop, web, Android, and iOS applications. Working on AI-powered solutions, LLM applications, Agentic AI integration, and intelligent automation.',
        current=True, order=1
    )

if not Education.objects.exists():
    Education.objects.create(
        degree='B.Tech in Computer Science and Engineering',
        institution='Pranveer Singh Institute of Technology, Kanpur',
        year='2022 - 2026',
        description='CGPA: 7.03 | Specialized in Software Engineering, AI, and Web Development. Solved 999+ DSA problems on LeetCode. Passionate about building intelligent software systems.',
        order=1
    )
print('Data seeded.')
"
