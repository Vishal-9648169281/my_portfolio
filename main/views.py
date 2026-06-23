from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone
from .models import Profile, Skill, Project, Experience, Education, Contact


def send_contact_email(name, email, subject, message):
    """Send two emails:
       1. To Vishal  — full details of the new inquiry
       2. To sender  — auto-reply confirmation
    """
    now = timezone.now().strftime("%d %b %Y, %I:%M %p")

    # ── 1. Notification email TO VISHAL ──────────────────────
    owner_subject = f"[Portfolio] New Message: {subject}"

    owner_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{ margin:0; padding:0; background:#0a0a14; font-family:'Segoe UI',Arial,sans-serif; }}
  .wrap {{ max-width:600px; margin:30px auto; background:#111120; border-radius:16px; overflow:hidden; border:1px solid rgba(124,58,237,.25); }}
  .header {{ background:linear-gradient(135deg,#7c3aed,#06b6d4); padding:32px 36px; }}
  .header h1 {{ margin:0; color:#fff; font-size:22px; font-weight:700; }}
  .header p {{ margin:6px 0 0; color:rgba(255,255,255,.75); font-size:13px; }}
  .badge {{ display:inline-block; background:rgba(255,255,255,.2); color:#fff; padding:4px 12px; border-radius:20px; font-size:11px; font-weight:600; margin-top:10px; }}
  .body {{ padding:32px 36px; }}
  .field {{ margin-bottom:20px; }}
  .label {{ font-size:10px; color:#7c6fa0; text-transform:uppercase; letter-spacing:.1em; font-weight:600; margin-bottom:6px; }}
  .value {{ background:#1a1a2e; border:1px solid rgba(124,58,237,.2); border-radius:10px; padding:12px 16px; color:#e2e0f0; font-size:14px; line-height:1.6; }}
  .value a {{ color:#a78bfa; text-decoration:none; }}
  .message-box {{ background:#1a1a2e; border:1px solid rgba(124,58,237,.2); border-left:3px solid #7c3aed; border-radius:10px; padding:16px; color:#d0cee8; font-size:14px; line-height:1.7; white-space:pre-wrap; }}
  .actions {{ text-align:center; margin:24px 0 8px; }}
  .btn {{ display:inline-block; background:linear-gradient(135deg,#7c3aed,#06b6d4); color:#fff; padding:12px 28px; border-radius:50px; text-decoration:none; font-weight:600; font-size:14px; }}
  .footer {{ background:#0d0d1a; padding:16px 36px; text-align:center; color:#4a4870; font-size:11px; border-top:1px solid rgba(255,255,255,.05); }}
</style>
</head>
<body>
<div class="wrap">
  <div class="header">
    <h1>New Portfolio Message</h1>
    <p>Someone reached out through your portfolio contact form</p>
    <span class="badge">Received: {now} IST</span>
  </div>
  <div class="body">
    <div class="field">
      <div class="label">From</div>
      <div class="value"><strong style="color:#a78bfa">{name}</strong></div>
    </div>
    <div class="field">
      <div class="label">Email</div>
      <div class="value"><a href="mailto:{email}">{email}</a></div>
    </div>
    <div class="field">
      <div class="label">Subject</div>
      <div class="value">{subject}</div>
    </div>
    <div class="field">
      <div class="label">Message</div>
      <div class="message-box">{message}</div>
    </div>
    <div class="actions">
      <a href="mailto:{email}?subject=Re: {subject}" class="btn">Reply to {name}</a>
    </div>
  </div>
  <div class="footer">
    Vishal Yadav Portfolio &mdash; vishalyaduvansi8081@gmail.com &mdash; +91-9648169281
  </div>
</div>
</body>
</html>
"""

    owner_text = f"""
New Portfolio Contact Message
==============================
From    : {name}
Email   : {email}
Subject : {subject}
Time    : {now}

Message:
{message}

-- Reply: mailto:{email}
"""

    msg1 = EmailMultiAlternatives(
        subject=owner_subject,
        body=owner_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.OWNER_EMAIL],
        reply_to=[email],
    )
    msg1.attach_alternative(owner_html, "text/html")
    msg1.send(fail_silently=True)

    # ── 2. Auto-reply email TO SENDER ────────────────────────
    reply_subject = f"Thank you for visiting my portfolio, {name.split()[0]}!"

    reply_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {{ margin:0; padding:0; background:#0a0a14; font-family:'Segoe UI',Arial,sans-serif; }}
  .wrap {{ max-width:600px; margin:30px auto; background:#111120; border-radius:16px; overflow:hidden; border:1px solid rgba(124,58,237,.25); }}
  .header {{ background:linear-gradient(135deg,#7c3aed,#06b6d4); padding:36px; text-align:center; }}
  .avatar {{ width:72px; height:72px; background:rgba(255,255,255,.15); border-radius:50%; margin:0 auto 14px; display:flex; align-items:center; justify-content:center; font-size:28px; font-weight:800; color:#fff; letter-spacing:-1px; }}
  .header h1 {{ margin:0; color:#fff; font-size:22px; font-weight:700; }}
  .header p {{ margin:8px 0 0; color:rgba(255,255,255,.75); font-size:13px; }}
  .body {{ padding:32px 36px; color:#c8c6e0; font-size:15px; line-height:1.7; }}
  .highlight {{ background:rgba(124,58,237,.1); border:1px solid rgba(124,58,237,.2); border-radius:10px; padding:16px; margin:20px 0; color:#a78bfa; font-size:13px; }}
  .summary {{ background:#1a1a2e; border-radius:10px; padding:16px 20px; margin:20px 0; }}
  .summary p {{ margin:4px 0; font-size:13px; color:#9896b8; }}
  .summary span {{ color:#e2e0f0; font-weight:500; }}
  .links {{ display:flex; gap:12px; justify-content:center; margin:24px 0; }}
  .link-btn {{ display:inline-block; padding:10px 20px; border-radius:50px; text-decoration:none; font-size:13px; font-weight:600; }}
  .link-gh {{ background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.15); color:#e2e0f0; }}
  .link-li {{ background:rgba(10,102,194,.2); border:1px solid rgba(10,102,194,.4); color:#60a5fa; }}
  .footer {{ background:#0d0d1a; padding:16px 36px; text-align:center; color:#4a4870; font-size:11px; border-top:1px solid rgba(255,255,255,.05); }}
</style>
</head>
<body>
<div class="wrap">
  <div class="header">
    <div class="avatar">VY</div>
    <h1>Thank You for Visiting!</h1>
    <p>I will respond to you as soon as possible</p>
  </div>
  <div class="body">
    <p>Hi <strong style="color:#a78bfa">{name.split()[0]}</strong>,</p>
    <p>Thank you for visiting my portfolio and reaching out! I have received your message and I will <strong style="color:#22d3ee">respond as soon as possible</strong>.</p>

    <div class="highlight">
      Your message has been safely received. I appreciate you taking the time to contact me and I look forward to connecting with you!
    </div>

    <p style="color:#9896b8; font-size:13px;">Here's a summary of what you sent:</p>
    <div class="summary">
      <p>Subject: <span>{subject}</span></p>
      <p>Sent on: <span>{now} IST</span></p>
      <p>Your email: <span>{email}</span></p>
    </div>

    <p>In the meantime, feel free to check out my work or connect with me:</p>

    <div class="links">
      <a href="https://github.com/Vishal-9648169281" class="link-btn link-gh">GitHub Profile</a>
      <a href="https://www.linkedin.com/in/vishalyadavdev/" class="link-btn link-li">LinkedIn</a>
    </div>

    <p style="margin-top:24px;">Best regards,<br>
    <strong style="color:#a78bfa">Vishal Yadav</strong><br>
    <span style="font-size:12px; color:#6b6990;">Full Stack Developer &amp; AI Engineer | CTC Chandigarh</span>
    </p>
  </div>
  <div class="footer">
    This is an automated reply from Vishal Yadav's Portfolio.<br>
    vishalyaduvansi8081@gmail.com &nbsp;|&nbsp; +91-9648169281 &nbsp;|&nbsp; Kanpur, UP, India
  </div>
</div>
</body>
</html>
"""

    reply_text = f"""
Hi {name.split()[0]},

Thank you for visiting my portfolio and reaching out!
I have received your message and will respond as soon as possible.

Your message summary:
Subject : {subject}
Sent on : {now}

Connect with me:
GitHub   : https://github.com/Vishal-9648169281
LinkedIn : https://www.linkedin.com/in/vishalyadavdev/

Best regards,
Vishal Yadav
Full Stack Developer & AI Engineer
"""

    msg2 = EmailMultiAlternatives(
        subject=reply_subject,
        body=reply_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
        reply_to=[settings.OWNER_EMAIL],
    )
    msg2.attach_alternative(reply_html, "text/html")
    msg2.send(fail_silently=False)


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    skill_categories = {
        'frontend': skills.filter(category='frontend'),
        'backend': skills.filter(category='backend'),
        'database': skills.filter(category='database'),
        'tools': skills.filter(category='tools'),
    }

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            # Save to DB
            Contact.objects.create(
                name=name, email=email,
                subject=subject, message=message
            )
            # Send emails
            try:
                send_contact_email(name, email, subject, message)
            except Exception:
                pass  # DB save succeeded; email failure is silent
            messages.success(request, f'Message sent! I will reply to {email} within 24 hours.')
        else:
            messages.error(request, 'Please fill all the fields.')
        return redirect('home')

    context = {
        'profile': profile,
        'skills': skills,
        'skill_categories': skill_categories,
        'projects': projects,
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'main/index.html', context)
