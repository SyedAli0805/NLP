import spacy

nlp = spacy.load("en_core_web_sm")

# News Article
text = """
In an office note, the CJP regretted about the issuance of the clarification and summoned an 
explanation from the respective officers of the court. Authored by senior puisne judge Justice 
Syed Mansoor Ali Shah, the second clarification on Friday explained that the apex court had 
granted the relief in the July 12 short order to enforce the right of the electorate through 
political parties to have proportional representation in the reserved seats under paragraphs (d) and (e) of 
Article 51(6) and paragraph (c) of clause (3) of Article 106 of the Constitution. Issued on Saturday, 
the fresh office note by the CJP stated that it was reported that a clarification was issued on Oct 18 by 
eight judges when the CJP was in the midst of writing a judgement. “Therefore, I sent for the file but did 
not find the original of the said ‘clarification’ therein,” the note regretted.
It went on to say that the assistant registrar (implementation) issued a letter to the secretary of the 
Election Commission of Pakistan and the Pakistan Tehreek-i-Insaf (PTI) even though the 
original of the second clarification was not in the file. The officials were subsequently directed to submit 
their explanation suggesting why the said letter/notice was issued before it was filed in the office, the note
said. Likewise, the webmaster, Asim Javed, was also directed to explain why the second clarification was 
uploaded on the Supreme Court website on Oct 18 when the same had not been filed in the office.
On Sept 22, CJP Isa raised nine questions in a letter to the Supreme Court’s registrar, seeking clarification 
on how an earlier Sept 14 clarification order was uploaded on the top court’s website. The Sept 14 order, 
issued by the eight judges led by senior puisne judge Justice Syed Man­soor Ali Shah, had criticised the ECP 
for failing to implement the Supreme Court’s July 12 judgement, which declared the PTI eligible for reserved 
seats in parliament. In his letter dated Sept 21, the CJP wondered who had directed the uploading of the Sept 
14 clarification order on  the court’s website. His inquiry followed a note from the deputy registrar 
(Judicial), who flagged the issue of the order’s appearance on the website. The note questioned how the order 
was uploaded when no cause list had been issued, no notices had been sent to the parties, and the order had 
not been received by the deputy registrar’s office until 8pm on the day of its upload. CJP Isa’s letter to 
the registrar echoed the concerns raised in the deputy registrar’s note, stating that nine questions had 
arisen as a result of the development. Among the questions posed were: when were the applications for 
clarification filed, and why were they not presented before the three-judge committee established under the 
Supreme Court (Practice and Procedure) Act, 2023. He also inquired about how the applications were fixed for 
hearing without a cause list being issued and whether notices were served to the parties concerned, including 
the attorney general for Pakistan. The CJP had also questioned in which courtroom or chamber the applications 
were heard and by whom and why no cause list was issued for the announcement of the Sept 14 clarification 
order. He also asked how the order was uploaded on the Supreme Court’s website without first being deposited 
in the court’s original file. Lastly, the CJP demanded to know who had authorised the upload of the order.
"""


doc = nlp(text)

for ent in doc.ents:
    print(ent.text,"  ->  ",ent.label_)