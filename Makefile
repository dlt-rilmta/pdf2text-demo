URL=http://www.kozlonyok.hu/nkonline/MKPDF/hiteles/
PDFS=MK14091.pdf MK14180.pdf MK19057.pdf MK19065.pdf
pdfs=$(PDFS:%=pdf/%)


all: demo
.PHONY: all


$(pdfs): pdf/
	@echo -e '\nDownload $@'
	@cd pdf/ ; curl $(URL)$(@:pdf/%=%) -O


pdf/:
	@mkdir -p $@


demo: demo.py $(pdfs)
	@pipenv run python3 $<
.PHONY: demo


clean:
	rm -rf pdf/
	rm -rf txt/
.PHONY: clean

