""" Find the number of different addresses that actually receive mails """
def num_unique_emails(emails):
    receive_emails = []

    for email in emails:
        local_name, domain = email.split('@')
        local_name = local_name.split('+')[0].replace('.', '')

        new_email = local_name + '@' + domain

        if new_email not in receive_emails:
            receive_emails.append(local_name + '@' + domain)
    return len(receive_emails)


# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# output 2,  "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

emails_lst = list(map(str, input('Enter list elements: ').split()))

print(num_unique_emails(emails_lst))