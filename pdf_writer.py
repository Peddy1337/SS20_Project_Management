from pdfdocument.document import PDFDocument
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

class PDFWriter :

    # set newline when a string has a certain length 
    def adjustStringLength(self,string) :
        if(len(string) > 20) :
           spaceIndex = string.rfind(' ',0,20)
           hyphenIndex = string.rfind('-',0,20)
           commaIndex = string.rfind(',',0,20)           
           string = string[0:max(spaceIndex,hyphenIndex,commaIndex)]+'\n'+string[max(spaceIndex,hyphenIndex,commaIndex)+1:len(string)]

        return string

    # generate pdf file in logbook format
    def writeToPDF(self,path,data) :
        pdf = PDFDocument(path)
        pdf.init_report()
        pdf.generate_style()

        pdf.style.heading1.alignment = TA_CENTER
        pdf.style.heading1.fontSize = 18
        heading_style = pdf.style.heading1
        
        pdf.h1('Fahrtenbuch Firma RAC', style = heading_style)

        pdf.p('\n\n\n')
        
        content = [['Name', 'Datum','Anfangskilometerstand','Endkilometerstand',
                    'gefahrene Kilometer','Art der Fahrt','Zweck der Fahrt',
                    'Fahrtanfang','Fahrtziel']]
        for p in data['rides'] :
            row = []
            for d in p :
                if(d != 'Bestaetigt') : 
                    row.append(self.adjustStringLength(p.get(d)))
            content.append(row)

        # ReportLab formatting
        table_style = (
            ("FONT", (0, 0), (-1, -1), "%s" % pdf.style.fontName, 4),
            ("TOPPADDING", (0, 0), (-1, -1), 2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            (
                "FONT",
                (0, 0),
                (-1, 0),
                "%s-Bold" % pdf.style.fontName,
                4.5,
            ),)

        header = [['KFZ-Kennzeichen','Anfangsdatum','Enddatum'],
                  [data['header'][0]['KFZ-Kennzeichen'],data['header'][0]['Anfangsdatum'],data['header'][0]['Enddatum']]]
        header2 = [['Anfangskilometerstand','Endkilometerstand'],
                  [data['header'][0]['Anfangskilometerstand'],data['header'][0]['Endkilometerstand']]]
        

        pdf.table(header,80,style = table_style)
        pdf.table(header2,80,style = table_style)
        pdf.p('\n\n\n')
        pdf.table(content,60,style = table_style)
        pdf.generate()


