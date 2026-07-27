---
Architechture URL :- https://www.tldraw.com/f/faJganF5s9zVV-_ggRgEy?d=v-1555.491.3771.2150.page
---

---
We have two type of data
1. Raw Data
2. Noisy Data

Raw data is related to k8's and Noisy data is anything not related to k8's
---

---
We have different type of data like
1. PDF
2. HTML
3. TXT
4. DOCX/PPTX

So we will have to use different tools to parse that data
---

---
__init__.py file is used to tell the compiler that its a module.
---

---
app/ingestion/loaders

This loader will handle the loading of the different type of data. This is our smart parser
---

---
app/ingestion/chunking

This will handle the chunking of the data
---

---
app/ingestion/processor.py

This will handle all the processed of loading and chunking the data i.e. It will process the full ingestion pipeline.
---