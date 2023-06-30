import pywhatkit as pwk

# Generate handwritten text
text = "Narender Singh ko mera Namste Jay baba ki"
pwk.text_to_handwriting(text, save_to="handwritten.png")
