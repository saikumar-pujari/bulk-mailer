import smtplib
import csv
import time
import os
from dotenv import load_dotenv
load_dotenv()
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, CSV_FILE_PATH

SUBJECT = "You Are Invited: NEXUS SPRING OF CODE 2026 (NSoC) 🎉"

def get_html_template(name="Developer"):
    return f"""
    <div dir="ltr">
      <table border="0" cellpadding="0" cellspacing="0" width="100%" style="color:rgb(15,23,42);font-family:'Plus Jakarta Sans',system-ui,sans-serif;font-size:medium;background-color:rgb(243,246,249);border-collapse:collapse">
        <tbody>
          <tr>
            <td align="center" style="padding:50px 10px">
              <table border="0" cellpadding="0" cellspacing="0" width="650" style="background-color:rgb(255,255,255);border-radius:64px;overflow:hidden;border-collapse:collapse">
                <tbody>
                  <tr>
                    <td align="center" style="padding:60px 40px 0px">
                      <img src="https://nsoc.in/logo.png" width="120" alt="NSoC Logo" style="border: 0px; height: auto; line-height: 16px; outline: none; width: 120px;">
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="padding:40px 40px 0px"><b>You Are Invited</b></td>
                  </tr>
                  <tr>
                    <td align="center" style="padding:40px 50px">
                      <h1 style="margin:0px;font-family:'Space Grotesk',sans-serif;font-size:48px;letter-spacing:-2px;line-height:0.95">
                        NEXUS SPRING<br><span style="color:rgb(16,185,129)">OF CODE 2026</span>
                      </h1>
                      <p style="margin:25px 0px 0px;font-size:18px;line-height:1.7;color:rgb(71,85,105);max-width:500px">
                        A community-driven bridge to the future of open source.
                      </p>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0px 60px 50px">
                      <div style="border-left:4px solid rgb(16,185,129);padding-left:30px;margin-bottom:40px">
                        <p style="margin:0px 0px 15px;font-size:18px;font-weight:700">Hi {name},</p>
                        <p style="margin:0px;font-size:17px;line-height:1.8;color:rgb(71,85,105)">
                          We are top contributors from GSSoC, announcing the launch of&nbsp;<b style="color:rgb(16,185,129)">Nexus Spring of Code (NSoC)</b>.
                        </p>
                      </div>
                      <p style="margin:0px;font-size:17px;line-height:1.8;color:rgb(71,85,105)">
                        On behalf of top contributors and program managers from GSSoC, we invite you to be part of this strong open-source ecosystem.
                      </p>
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0px 40px 50px">
                      <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:rgb(248,250,252);border-radius:40px;padding:40px;border-collapse:collapse">
                        <tbody>
                          <tr>
                            <td align="center">
                              <h3 style="margin:0px 0px 30px;font-family:'Space Grotesk',sans-serif;font-size:22px">Exclusive Member Access:</h3>
                              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse">
                                <tbody>
                                  <tr>
                                    <td align="center" style="padding:10px">
                                      <div style="font-size:24px">💼</div>
                                      <p style="margin:5px 0px 0px;font-size:14px;font-weight:700;color:rgb(100,116,139)">Internships</p>
                                    </td>
                                    <td align="center" style="padding:10px">
                                      <div style="font-size:24px">🎁</div>
                                      <p style="margin:5px 0px 0px;font-size:14px;font-weight:700;color:rgb(100,116,139)">Rewards</p>
                                    </td>
                                    <td align="center" style="padding:10px">
                                      <div style="font-size:24px">🌐</div>
                                      <p style="margin:5px 0px 0px;font-size:14px;font-weight:700;color:rgb(100,116,139)">Domains</p>
                                    </td>
                                    <td align="center" style="padding:10px">
                                      <div style="font-size:24px">📧</div>
                                      <p style="margin:5px 0px 0px;font-size:14px;font-weight:700;color:rgb(100,116,139)">Hiring Access</p>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="padding:0px 50px 80px">
                      <div style="background-color:rgb(15,23,42);border-radius:48px;padding:60px 40px">
                        <h2 style="margin:0px 0px 40px;font-family:'Space Grotesk',sans-serif;font-size:32px;color:rgb(255,255,255)">Join our community here:</h2>
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse">
                          <tbody>
                            <tr>
                              <td style="padding:10px">
                                <a href="https://shorturl.at/9gLKy" target="_blank" style="color:rgb(255,255,255);display:block;background-color:rgb(16,185,129);padding:20px 30px;border-radius:20px;text-decoration-line:none;font-weight:800;font-size:15px;text-transform:uppercase;letter-spacing:1px">WhatsApp</a>
                              </td>
                              <td style="padding:10px">
                                <a href="https://shorturl.at/Eb1M0" target="_blank" style="color:rgb(255,255,255);display:block;background-color:rgb(88,101,242);padding:20px 30px;border-radius:20px;text-decoration-line:none;font-weight:800;font-size:15px;text-transform:uppercase;letter-spacing:1px">Discord</a>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="padding:0px 60px 80px">
                      <div style="border-top:1px solid rgb(241,245,249);padding-top:50px">
                        <p style="margin:0px 0px 10px;color:rgb(148,163,184);font-size:12px;text-transform:uppercase;letter-spacing:4px;font-weight:800">Best Regards</p>
                        <p style="margin:0px;color:rgb(16,185,129);font-size:24px;font-weight:800;font-family:'Space Grotesk',sans-serif">Team Nexus Spring of Code</p>
                      </div>
                      <div style="margin-top:60px;color:rgb(203,213,225);font-size:11px;letter-spacing:5px">&copy; 2026 NEXUS SPRING OF CODE</div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def send_bulk_emails():
    recipients = []
    try:
        with open(CSV_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                email = row.get('email', '').strip() #avoid duplication of code!
                if email:
                    full_name = row.get('full_name', '').strip() #if users enters ' '(space only) that will get reduce to ''
                    first_name = full_name.split()[0] if full_name else 'Developer' # check the nama here! 
                    recipients.append({
                        'email': email,
                        'name': first_name
                    })
    except FileNotFoundError:
        print(f"Error: Could not find {CSV_FILE_PATH}. Please create it first.")
        return

    # LIMIT TO FIRST MAX_EMAILS mails TO PREVENT GMAIL BAN
    MAX_EMAILS = 400
    #Google Limits to 500 mails only for Free acount and sending more than these will result in spam account!
    if len(recipients) > MAX_EMAILS:
        print(f"⚠️ Warning: Found {len(recipients)} emails in CSV.")
        print(f"🛡️ Safety cap engaged: Only sending to the first {MAX_EMAILS} to protect your Gmail account.")
        recipients = recipients[:MAX_EMAILS]

    total_emails = len(recipients)
    print(f"Starting sequence for {total_emails} email addresses...")

    try:
        print(f"🔄 Connecting to {SMTP_SERVER}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("✅ Successfully logged in to email server!\n")
    except Exception as e:
        print(f"Failed to connect or login: {e}")
        return

    success_count = 0
    fail_count = 0

    for index, person in enumerate(recipients, 1):
        recipient_email = person['email']
        recipient_name = person['name']
        
        try:
            msg = MIMEMultipart("alternative")
            msg['From'] = SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = SUBJECT

            html_content = get_html_template(recipient_name)
            msg.attach(MIMEText(html_content, 'html'))

            # Send the email
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            success_count += 1
            print(f"[{index}/{total_emails}] ✅ Sent to: {recipient_name} <{recipient_email}>")

            # SAFETY UPDATE: 2-Second delay
            time.sleep(2)

        except Exception as e:
            fail_count += 1
            print(f"[{index}/{total_emails}] Failed to send to {recipient_email}: {e}")

    # 4. Cleanup
    server.quit()
    print("\n" + "="*40)
    print("FINISHED!")
    print(f"Total Sent Successfully: {success_count}")
    print(f"Total Failed: {fail_count}")
    print("="*40)

if __name__ == "__main__":
    send_bulk_emails()
