import unittest
import ps4b
import ps4c
import tracemalloc

tracemalloc.start()
class ProblemSet4BTest(unittest.TestCase):
    
    def test_plaintext(self):
        self.assertEqual(ps4b.PlaintextMessage('hello', 2).get_message_text_encrypted(), "jgnnq")
        self.assertEqual(ps4b.PlaintextMessage('Great!', 4).get_message_text_encrypted(), 'Kviex!')

    def test_ciphertext(self):
        self.assertEqual(ps4b.CiphertextMessage('jgnnq').decrypt_message(), (24, 'hello'))
        self.assertEqual(ps4b.CiphertextMessage('Kviex!').decrypt_message(), (22, 'Great!'))

class ProblemSet4CTest(unittest.TestCase):

    def test_init_submessage(self):
        test_submessage = ps4c.SubMessage("hello")
        self.assertEqual(test_submessage.get_message_text(), "hello", "Get Message Text Init Failed for SubMessage Class")
    
    def test_init_encryptedsubmessage(self):
        test_encryptedsubmessage = ps4c.EncryptedSubMessage("hello")
        self.assertEqual(test_encryptedsubmessage.get_message_text(), "hello", "Get Message Text Init Failed for EncryptedSubMessage Class")



    def test_submessage(self):
        # Set up Messages for Test Cases
        message1 = ps4c.SubMessage("Good Day!")
        message2 = ps4c.SubMessage("Has Been Great!")
        permutation = 'iouae'
        enc_dict = message1.build_transpose_dict(permutation)
        self.assertEqual(message1.apply_transpose(enc_dict), "Gaad Diy!", "Encoding of Message 1 failed")
        self.assertEqual(message2.apply_transpose(enc_dict), "His Boon Groit!", "Encoding of Message 2 failed")

    def test_encryptedsubmessage(self):
        # Set up Messages for Test Cases
        message1 = ps4c.EncryptedSubMessage("Gaad Diy!")
        message2 = ps4c.EncryptedSubMessage("His Boon Groit!")
        message3 = ps4c.EncryptedSubMessage("Grooitten")
        self.assertEqual(message1.decrypt_message(), "Good Day!", "Decryption of Message 1 failed")
        self.assertEqual(message2.decrypt_message(), "Has Been Great!", "Decryption of Message 2 failed")
        self.assertEqual(message3.decrypt_message(), "Grooitten", "Decrypt does not leave original text alone if no decryption found")


if __name__ == '__main__':
    unittest.main()