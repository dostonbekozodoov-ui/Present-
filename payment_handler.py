import base64

class PaymentHandler:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt_card_info(self, card_info):
        # Encryption using base64
        card_info_bytes = card_info.encode('utf-8')
        encrypted_info = base64.b64encode(card_info_bytes).decode('utf-8')
        return encrypted_info

    def validate_card(self, card_number):
        # Luhn algorithm for card validation
        num = [int(d) for d in str(card_number)]
        checksum = 0
        reverse_num = num[::-1]
        for i in range(len(reverse_num)):
            if i % 2 == 1:
                double = reverse_num[i] * 2
                checksum += double - 9 if double > 9 else double
            else:
                checksum += reverse_num[i]
        return checksum % 10 == 0

    def process_payment(self, card_info, amount):
        card_number = card_info['number']
        if not self.validate_card(card_number):
            return False, "Invalid card number"
        encrypted_card = self.encrypt_card_info(card_number)
        print(f'Processing payment: {amount} so\'m')
        return True, f"Payment successful! {amount} so\'m charged"