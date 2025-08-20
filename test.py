from hazm_normalizer import Normalizer

# Initialize the Normalizer class
normalizer = Normalizer()

# Persian text to normalize
text = """
اصلاح نويسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند و حروف عربي استفاده شده غلط مانند کُ و ي را حذف می‌کند.
"""

# Normalize the text
result = normalizer.normalize(text)

print(result)
'اصلاح نویسه‌ها و استفاده از نیم‌فاصله پردازش را آسان می‌کند و حروف عربی استفاده‌شده غلط مانند ک و‌ ی را حذف می‌کند. '