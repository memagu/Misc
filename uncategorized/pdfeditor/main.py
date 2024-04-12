from datetime import datetime
from pathlib import Path
import re



PATH_TEMPLATE_PDF = Path(r"./Simon Linder - Personligt Brev [mall].pdf")
PATH_STORES = Path(r"./stores.txt")
PATH_OUTPUT = Path(r"./output/")
SYMBOL_STORE = "[Matbutikskedja]"
SYMBOL_FRANCHISE = "[Matbutikskedja]"
SYMBOL_DATE = "[datum]"

if not PATH_OUTPUT.exists():
    PATH_OUTPUT.mkdir(parents=True, exist_ok=True)

with open(PATH_TEMPLATE_PDF, "rb") as f:
    template = PDF.loads(f)

template = template



template = ap.Document(str(PATH_TEMPLATE_PDF))

# text_absorber_store = ap.text.TextFragmentAbsorber(SYMBOL_STORE)
# text_absorber_franchise = ap.text.TextFragmentAbsorber(SYMBOL_FRANCHISE)
text_absorber_date = ap.text.TextFragmentAbsorber(SYMBOL_DATE)

# template.pages.accept(text_absorber_store)
# template.pages.accept(text_absorber_franchise)
template.pages.accept(text_absorber_date)

# text_fragments_store = text_absorber_store.text_fragments
# text_fragments_franchise = text_absorber_franchise.text_fragments
text_fragments_date = text_absorber_date.text_fragments


date = datetime.today().strftime("%Y-%m-%d")
with open(PATH_STORES, "r", encoding="UTF-8") as f:
    for store, franchise in ((store := re.sub(r"\(.*\)", '', line.strip()), store.split(maxsplit=1)[0]) for line in f.readlines()):
        for i in range(1, min(4, len(text_fragments_date) + 1)):
            text_fragments_date[i].text = date

        # for text_framgent in text_fragments_date:
        #     text_framgent.text = date
        #
        # for text_framgent in text_fragments_store:
        #     text_framgent.text = store
        #
        # for text_framgent in text_fragments_franchise:
        #     text_framgent.text = franchise

        template.save(str(PATH_OUTPUT / store / ".pdf"))
        break