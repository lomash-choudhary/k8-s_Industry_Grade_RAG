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

---
Tools used to extract data from the website

1. BeautifulSoup
2. Firecrawl
3. Crawl AI
---

---
If query Dimension and the Vector DB ingested data dimesions differ then you won't be able to do the cosine similarity search and will have to add the meta data filtering based on the
user query dimesion.

In the prod we will maintain the dimesions during the retirval we won't be performing similarity searches on the two different dimesions.
---

---
Q: How to handle PDF's that have images with text under it.
A: Generally using captioning, most of the recent layout detection models can handle that, the New PP Doc layout its open source at hugging face, and YOLO Doc layout model also
works really great.
---

---
BM25 is a sparse vector based search algorithm.
---

---
Best Chunking Strategy
If we talk about overall multi modal perpective
1. Layout Aware chunking or context aware chunking
2. Semantic based chunking and rest all chunking strategies.
---

---
Logfire is a observibility tool for the developers
----