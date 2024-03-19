import pywhatkit as pw

txt="""We specialize in designing and developing custom websites
that are not only visually stunning but also highly functional. Let us help you take your online presence to the next level."""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" END ")
