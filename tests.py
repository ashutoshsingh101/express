import re
name_data = [[([[{'y1': 19, 'y0': 0, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 19, 'y0': 0, 'x0': 11, 'x1': 1000, 'text': ''}],
       [{'y1': 262, 'y0': 19, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 262, 'y0': 19, 'x0': 11, 'x1': 1000, 'text': u'express\nclinics\nmr number: egin17177474\npatient name:\ngender : female\nid\nrefby\na joint venture with davita inc., a fortune 500 company\ncentre : indirapuram sample no : 1706121 1681\n:51074323 collection on : 15/6/2017 10:16:01am\nage :41.11 years received on : 15/6/2017 10:16:01am\nreported on : 15/6/2017 151:29pm\n:\n:religare\n'}]])], [([[{'y1': 19, 'y0': 0, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 19, 'y0': 0, 'x0': 11, 'x1': 1000, 'text': ''}],
       [{'y1': 262, 'y0': 19, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 262, 'y0': 19, 'x0': 11, 'x1': 1000, 'text': u'express\nclinics\nmr number: egin17177474\npatient name:\ngender : female\nid\nrefby\na joint venture with davita inc., a fortune 500 company\ncentre : indirapuram sample no: 1706121 16811\n:51074323 collection on : 15/6/2017 10:16:01am\nage :41.11 years received on : 15/6/2017 10:16:01am\nreported on : 15/6/2017 1:50:45pm\n:religare\n'}]])], [([[{'y1': 19, 'y0': 0, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 19, 'y0': 0, 'x0': 11, 'x1': 1000, 'text': ''}],
       [{'y1': 262, 'y0': 19, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 262, 'y0': 19, 'x0': 11, 'x1': 1000, 'text': u'express\nclinics\nmr number: egin17177474\npatient name:\ngender : female\nid\nrefby\na joint venture with davita inc., a fortune 500 company\ncentre : indirapuram sample no : 1706121 1681\n:51074323 collection on : 15/6/2017 10:16:01am\nage :41.11 years received on : 15/6/2017 10:16:01am\nreported on : 15/6/2017 12:53:20pm\n:religare\n'}]])], [([[{'y1': 19, 'y0': 0, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 19, 'y0': 0, 'x0': 11, 'x1': 1000, 'text': ''}],
       [{'y1': 262, 'y0': 19, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 262, 'y0': 19, 'x0': 11, 'x1': 1000, 'text': u'express\nclinics\nmr number: egin17177474\npatient name :\ngender : female\nid\nrefby\na joint venture with davita inc., a fortune 500 company\ncentre : indirapuram sample no : 1706121 1681\n:51074323 collection on : 15/6/2017 10:16:01am\nage :41.11 years received on : 15/6/2017 10:16:01am\nreported on : 15/6/2017 1:51:51pm\n:religare\n'}]])], [([[{'y1': 19, 'y0': 0, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 19, 'y0': 0, 'x0': 11, 'x1': 1000, 'text': ''}],
       [{'y1': 262, 'y0': 19, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 262, 'y0': 19, 'x0': 11, 'x1': 1000, 'text': u'express\nclinics\nmr number: egin17177474\npatient name:\ngender : female\nid\nrefby\na joint venture with davita inc., a fortune 500 company\ncentre : indirapuram sample no : 1706121 1681\n:51074323 collection on : 15/6/2017 10:16:01am\nage :41.11 years received on : 15/6/2017 10:16:01am\nreported on : 15/6/2017 1:52:45pm\n:religare\n'}]])], [([[{'y1': 19, 'y0': 0, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 19, 'y0': 0, 'x0': 11, 'x1': 1000, 'text': ''}],
       [{'y1': 262, 'y0': 19, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 262, 'y0': 19, 'x0': 11, 'x1': 1000, 'text': u'express\nclinics\nmr number: egin17177474\npatient name:\ngender : female\nid\nrefby\na joint venture with davita inc., a fortune 500 company\ncentre : indirapuram sample no : 1706121 1681\n:51074323 collection on : 15/6/2017 10:16:01am\nage :41.11 years received on : 15/6/2017 10:16:01am\nreported on : 15/6/2017 1:5117pm\n:religare\n'}]])]]







test_data = [[([[{'y1': 283, 'y0': 262, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 283, 'y0': 262, 'x0': 11, 'x1': 1000, 'text': u'bio-chemistry report\n'}],
       [{'y1': 326, 'y0': 283, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 326, 'y0': 283, 'x0': 11, 'x1': 1000, 'text': u'test name\nrenal function test (mln panel\nresults\nunits\nnormal range\n'}],
       [{'y1': 345, 'y0': 326, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 345, 'y0': 326, 'x0': 11, 'x1': 1000, 'text': u'blood urea level\n13.2\nmg/dl\n17 - 49\n'}]]), ([[{'y1': 348, 'y0': 345, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 348, 'y0': 345, 'x0': 20, 'x1': 258, 'text': ''},
        {'y1': 348, 'y0': 345, 'x0': 258, 'x1': 502, 'text': ''},
        {'y1': 348, 'y0': 345, 'x0': 502, 'x1': 692, 'text': u''},
        {'y1': 348, 'y0': 345, 'x0': 692, 'x1': 1000, 'text': ''}],
       [{'y1': 370, 'y0': 348, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 370, 'y0': 348, 'x0': 20, 'x1': 258, 'text': u'creatinine\n'},
        {'y1': 370, 'y0': 348, 'x0': 258, 'x1': 502, 'text': u'0.68\n'},
        {'y1': 370, 'y0': 348, 'x0': 502, 'x1': 692, 'text': u'mg/dl\n'},
        {'y1': 370, 'y0': 348, 'x0': 692, 'x1': 1000, 'text': u'0.6 - 1. 1\n'}],
       [{'y1': 388, 'y0': 370, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 388, 'y0': 370, 'x0': 20, 'x1': 258, 'text': u'uric acid\n'},
        {'y1': 388, 'y0': 370, 'x0': 258, 'x1': 502, 'text': u'5.3\n'},
        {'y1': 388, 'y0': 370, 'x0': 502, 'x1': 692, 'text': u'mg/dl\n'},
        {'y1': 388, 'y0': 370, 'x0': 692, 'x1': 1000, 'text': u'1.9 - 7.5\n'}]]), ([[{'y1': 669, 'y0': 388, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 669, 'y0': 388, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1068, 'y0': 669, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1068, 'y0': 669, 'x0': 11, 'x1': 1000, 'text': u'fierified by a re eased b;\ndrreddy\nin dipatrology, reg ta, 384\n'}],
       [{'y1': 1086, 'y0': 1068, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1086, 'y0': 1068, 'x0': 11, 'x1': 1000, 'text': u''}]]), ([[{'y1': 1088, 'y0': 1086, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1088, 'y0': 1086, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1134, 'y0': 1088, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1134, 'y0': 1088, 'x0': 11, 'x1': 1000, 'text': u"page 4 of 6\nindia's fastest growing multispeciality clinic & diagnostics chain\n"}]]), ([[{'y1': 1147, 'y0': 1134, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1147, 'y0': 1134, 'x0': 13, 'x1': 1000, 'text': u'e - space building, a-2 wing, 2nd floor, pune nagar road, vadgaonsnet, pune 4014.\n'}]]), ([[{'y1': 1175, 'y0': 1147, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1175, 'y0': 1147, 'x0': 13, 'x1': 1000, 'text': u'o: 1800-267-91910 9191@expressclinics.in\n'}]]), ([[{'y1': 1199, 'y0': 1175, 'x0': 0, 'x1': 133, 'text': u''},
        {'y1': 1199, 'y0': 1175, 'x0': 133, 'x1': 388, 'text': u'e consultations\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 388, 'x1': 512, 'text': u'diagnostics\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 512, 'x1': 650, 'text': u's * healthchecks\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 650, 'x1': 1000, 'text': u'pathology\n'}]]), ([{'y1': 1200, 'y0': 1199, 'x0': 0, 'x1': 1000, 'text': ''}])], [([[{'y1': 283, 'y0': 262, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 283, 'y0': 262, 'x0': 11, 'x1': 1000, 'text': u'bio-chemistry report\n'}],
       [{'y1': 326, 'y0': 283, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 326, 'y0': 283, 'x0': 11, 'x1': 1000, 'text': u'test name results\nplasma glucose - fasting - (god-pod method )\nunits\nnormal range\n'}],
       [{'y1': 648, 'y0': 326, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 648, 'y0': 326, 'x0': 11, 'x1': 1000, 'text': u'plasma glucose - fasling - (god-pod method) 99.0\nmg/dl\n<< 100 mg/dl\n'}],
       [{'y1': 1068, 'y0': 648, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1068, 'y0': 648, 'x0': 11, 'x1': 1000, 'text': u'fierified b& re eaad b;\ndr. reddy\nin dipatrology, reg ta, 384\n'}],
       [{'y1': 1086, 'y0': 1068, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1086, 'y0': 1068, 'x0': 11, 'x1': 1000, 'text': u''}]]), ([[{'y1': 1088, 'y0': 1086, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1088, 'y0': 1086, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1134, 'y0': 1088, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1134, 'y0': 1088, 'x0': 11, 'x1': 1000, 'text': u"page 2 of 6\nindia's fastest growing multispeciality clinic & diagnostics chain\n"}]]), ([[{'y1': 1147, 'y0': 1134, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1147, 'y0': 1134, 'x0': 13, 'x1': 1000, 'text': u'e - space building, a-2 wing, 2nd floor, pune nagar road, vadgaonsnet, pune 4014.\n'}]]), ([[{'y1': 1175, 'y0': 1147, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1175, 'y0': 1147, 'x0': 13, 'x1': 1000, 'text': u'o: 1800-267-91910 9191@expressclinics.in\n'}]]), ([[{'y1': 1199, 'y0': 1175, 'x0': 0, 'x1': 133, 'text': u''},
        {'y1': 1199, 'y0': 1175, 'x0': 133, 'x1': 388, 'text': u'e consultations\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 388, 'x1': 512, 'text': u'diagnostics\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 512, 'x1': 650, 'text': u's * healthchecks\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 650, 'x1': 1000, 'text': u'pathology\n'}]]), ([{'y1': 1200, 'y0': 1199, 'x0': 0, 'x1': 1000, 'text': ''}])], [([[{'y1': 283, 'y0': 262, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 283, 'y0': 262, 'x0': 11, 'x1': 1000, 'text': u'clinical pathology report\n'}],
       [{'y1': 343, 'y0': 283, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 343, 'y0': 283, 'x0': 11, 'x1': 1000, 'text': u'test name\nresults\nunits\nnormal range\nurine routine-urine\nphysical - examination\n'}],
       [{'y1': 367, 'y0': 343, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 367, 'y0': 343, 'x0': 11, 'x1': 1000, 'text': u'quantity examined\n20\nml\n5 - 30\n'}],
       [{'y1': 388, 'y0': 367, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 388, 'y0': 367, 'x0': 11, 'x1': 1000, 'text': u'appearance\nhazy\nclear\n'}],
       [{'y1': 409, 'y0': 388, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 409, 'y0': 388, 'x0': 11, 'x1': 1000, 'text': u'colour\npale yellow\npale yellow\n'}],
       [{'y1': 432, 'y0': 409, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 432, 'y0': 409, 'x0': 11, 'x1': 1000, 'text': u'ph\n5.5\n5 - 8.5\n'}],
       [{'y1': 471, 'y0': 432, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 471, 'y0': 432, 'x0': 11, 'x1': 1000, 'text': u'specific gravity\nchemical - examination\n1.005\n1.005 - 1.035\n'}],
       [{'y1': 495, 'y0': 471, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 495, 'y0': 471, 'x0': 11, 'x1': 1000, 'text': u'albumin\nabsent\nabsent\n'}],
       [{'y1': 516, 'y0': 495, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 516, 'y0': 495, 'x0': 11, 'x1': 1000, 'text': u'bile pigments\nabsent\nabsent\n'}],
       [{'y1': 538, 'y0': 516, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 538, 'y0': 516, 'x0': 11, 'x1': 1000, 'text': u'glucose\nabsent\nabsent\n'}],
       [{'y1': 560, 'y0': 538, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 560, 'y0': 538, 'x0': 11, 'x1': 1000, 'text': u'bile salts\nabsent\nabsent\n'}],
       [{'y1': 582, 'y0': 560, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 582, 'y0': 560, 'x0': 11, 'x1': 1000, 'text': u'ketone bodies\nabsent\nabsent\n'}],
       [{'y1': 604, 'y0': 582, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 604, 'y0': 582, 'x0': 11, 'x1': 1000, 'text': u'urobilinogen\nabsent\nabsent\n'}],
       [{'y1': 626, 'y0': 604, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 626, 'y0': 604, 'x0': 11, 'x1': 1000, 'text': u'blood\npresent 1+\nabsent\n'}],
       [{'y1': 665, 'y0': 626, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 665, 'y0': 626, 'x0': 11, 'x1': 1000, 'text': u'nitrate\nmicroscopic - examination\nabsent\nabsent\n'}],
       [{'y1': 690, 'y0': 665, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 690, 'y0': 665, 'x0': 11, 'x1': 1000, 'text': u'pus cells\n1-2\n/hpf\n1 -2\n'}],
       [{'y1': 711, 'y0': 690, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 711, 'y0': 690, 'x0': 11, 'x1': 1000, 'text': u'epithelial cells\n1-2\ni hpf\n3-4\n'}],
       [{'y1': 733, 'y0': 711, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 733, 'y0': 711, 'x0': 11, 'x1': 1000, 'text': u'r.b.cs\n2-4\ni hpf\nabsent\n'}],
       [{'y1': 754, 'y0': 733, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 754, 'y0': 733, 'x0': 11, 'x1': 1000, 'text': u'casts\nabsent\nabsent\n'}],
       [{'y1': 776, 'y0': 754, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 776, 'y0': 754, 'x0': 11, 'x1': 1000, 'text': u'crystals\nabsent\nabsent\n'}],
       [{'y1': 798, 'y0': 776, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 798, 'y0': 776, 'x0': 11, 'x1': 1000, 'text': u'bacteria\nabsent\nabsent\n'}],
       [{'y1': 828, 'y0': 798, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 828, 'y0': 798, 'x0': 11, 'x1': 1000, 'text': u'other findings\nabsent\nabsent\n'}],
       [{'y1': 902, 'y0': 828, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 902, 'y0': 828, 'x0': 11, 'x1': 1000, 'text': u'please correlate clinically.\n'}],
       [{'y1': 1068, 'y0': 902, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1068, 'y0': 902, 'x0': 11, 'x1': 1000, 'text': u'fierified by a re eased b;\ndrreddy\nh dpatrology, re, a 38-\n'}],
       [{'y1': 1086, 'y0': 1068, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1086, 'y0': 1068, 'x0': 11, 'x1': 1000, 'text': u''}]]), ([[{'y1': 1088, 'y0': 1086, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1088, 'y0': 1086, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1134, 'y0': 1088, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1134, 'y0': 1088, 'x0': 11, 'x1': 1000, 'text': u"page 1 of 6\nindia's fastest growing multispeciality clinic & diagnostics chain\n"}]]), ([[{'y1': 1147, 'y0': 1134, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1147, 'y0': 1134, 'x0': 13, 'x1': 1000, 'text': u'e - space building, a-2 wing, 2nd floor, pune nagar road, vadgaonsnet, pune 4014.\n'}]]), ([[{'y1': 1175, 'y0': 1147, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1175, 'y0': 1147, 'x0': 13, 'x1': 1000, 'text': u'o: 1800-267-91910 9191@expressclinics.in\n'}]]), ([[{'y1': 1199, 'y0': 1175, 'x0': 0, 'x1': 133, 'text': u''},
        {'y1': 1199, 'y0': 1175, 'x0': 133, 'x1': 388, 'text': u'e consultations\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 388, 'x1': 512, 'text': u'diagnostics\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 512, 'x1': 650, 'text': u's * healthchecks\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 650, 'x1': 1000, 'text': u'pathology\n'}]]), ([{'y1': 1200, 'y0': 1199, 'x0': 0, 'x1': 1000, 'text': ''}])], [([[{'y1': 326, 'y0': 262, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 326, 'y0': 262, 'x0': 11, 'x1': 1000, 'text': u'test name\nhemogram (cbc) + esr\ncomplete blood count (cbc) report\nresults units\nnormal range\n'}],
       [{'y1': 347, 'y0': 326, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 347, 'y0': 326, 'x0': 11, 'x1': 1000, 'text': u'total leucocyte\n9700\nicumm\n4000 - 10000\n'}],
       [{'y1': 370, 'y0': 347, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 370, 'y0': 347, 'x0': 11, 'x1': 1000, 'text': u'rbc count\n4.96\n10/6pl\n3.8 - 4.8\n'}],
       [{'y1': 388, 'y0': 370, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 388, 'y0': 370, 'x0': 11, 'x1': 1000, 'text': u'hemoglobin\n14.2\nomdl\n12 - 1\n'}]]), ([[{'y1': 392, 'y0': 388, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 392, 'y0': 388, 'x0': 20, 'x1': 268, 'text': u''},
        {'y1': 392, 'y0': 388, 'x0': 268, 'x1': 501, 'text': u''},
        {'y1': 392, 'y0': 388, 'x0': 501, 'x1': 692, 'text': u''},
        {'y1': 392, 'y0': 388, 'x0': 692, 'x1': 1000, 'text': u''}],
       [{'y1': 413, 'y0': 392, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 413, 'y0': 392, 'x0': 20, 'x1': 268, 'text': u'haematocrit\n'},
        {'y1': 413, 'y0': 392, 'x0': 268, 'x1': 501, 'text': u'43.0\n'},
        {'y1': 413, 'y0': 392, 'x0': 501, 'x1': 692, 'text': u''},
        {'y1': 413, 'y0': 392, 'x0': 692, 'x1': 1000, 'text': u'36 - 46\n'}],
       [{'y1': 434, 'y0': 413, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 434, 'y0': 413, 'x0': 20, 'x1': 268, 'text': u'mcv\n'},
        {'y1': 434, 'y0': 413, 'x0': 268, 'x1': 501, 'text': u'87\n'},
        {'y1': 434, 'y0': 413, 'x0': 501, 'x1': 692, 'text': u'fl\n'},
        {'y1': 434, 'y0': 413, 'x0': 692, 'x1': 1000, 'text': u'76-96\n'}],
       [{'y1': 457, 'y0': 434, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 457, 'y0': 434, 'x0': 20, 'x1': 268, 'text': u'mch\n'},
        {'y1': 457, 'y0': 434, 'x0': 268, 'x1': 501, 'text': u'28.7\n'},
        {'y1': 457, 'y0': 434, 'x0': 501, 'x1': 692, 'text': u'pg\n'},
        {'y1': 457, 'y0': 434, 'x0': 692, 'x1': 1000, 'text': u'27 - 32\n'}],
       [{'y1': 476, 'y0': 457, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 476, 'y0': 457, 'x0': 20, 'x1': 268, 'text': u'mchc\n'},
        {'y1': 476, 'y0': 457, 'x0': 268, 'x1': 501, 'text': u'33.1\n'},
        {'y1': 476, 'y0': 457, 'x0': 501, 'x1': 692, 'text': u'gm/dl\n'},
        {'y1': 476, 'y0': 457, 'x0': 692, 'x1': 1000, 'text': u'32 - 36\n'}]]), ([[{'y1': 480, 'y0': 476, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 480, 'y0': 476, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 500, 'y0': 480, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 500, 'y0': 480, 'x0': 11, 'x1': 1000, 'text': u'rdw\n11.4\n9.5 - 14.5\n'}],
       [{'y1': 540, 'y0': 500, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 540, 'y0': 500, 'x0': 11, 'x1': 1000, 'text': u'mpv\ndifferential count\n7.9\nf\n6 - 10\n'}],
       [{'y1': 563, 'y0': 540, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 563, 'y0': 540, 'x0': 11, 'x1': 1000, 'text': u'neutrophils\n64.7\n40 - 80\n'}],
       [{'y1': 585, 'y0': 563, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 585, 'y0': 563, 'x0': 11, 'x1': 1000, 'text': u'lymphocytes\n24.3\n20 - 40\n'}],
       [{'y1': 606, 'y0': 585, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 606, 'y0': 585, 'x0': 11, 'x1': 1000, 'text': u'monocytes\n7.6\n%\n2 10\n-\n'}],
       [{'y1': 628, 'y0': 606, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 628, 'y0': 606, 'x0': 11, 'x1': 1000, 'text': u'eosinophils\n2. 9\n1 - 6\n'}],
       [{'y1': 668, 'y0': 628, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 668, 'y0': 628, 'x0': 11, 'x1': 1000, 'text': u'basophils\nperipheral blood smear\n0.5\n< 1 -2\n'}],
       [{'y1': 692, 'y0': 668, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 692, 'y0': 668, 'x0': 11, 'x1': 1000, 'text': u'platelets\n320000\nlacs / cumm\n150000 - 410000\n'}],
       [{'y1': 714, 'y0': 692, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 714, 'y0': 692, 'x0': 11, 'x1': 1000, 'text': u'platelet morphology\nadequate on smear\nadequate on smear\n'}],
       [{'y1': 735, 'y0': 714, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 735, 'y0': 714, 'x0': 11, 'x1': 1000, 'text': u'wbc morphology\nwithin normal limit\nwithin normal limit\n'}],
       [{'y1': 775, 'y0': 735, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 775, 'y0': 735, 'x0': 11, 'x1': 1000, 'text': u'rbc morphology\nesr\nnormocytic normochromic\nnormocytic normochromic\n'}],
       [{'y1': 872, 'y0': 775, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 872, 'y0': 775, 'x0': 11, 'x1': 1000, 'text': u'e.s.r.\n13\nmmhr\n0 - 20\n'}],
       [{'y1': 1068, 'y0': 872, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1068, 'y0': 872, 'x0': 11, 'x1': 1000, 'text': u'fierified by a re eased b;\ndrreddy\nin dipatrology, reg ta, 384\n'}],
       [{'y1': 1086, 'y0': 1068, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1086, 'y0': 1068, 'x0': 11, 'x1': 1000, 'text': u''}]]), ([[{'y1': 1088, 'y0': 1086, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1088, 'y0': 1086, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1134, 'y0': 1088, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1134, 'y0': 1088, 'x0': 11, 'x1': 1000, 'text': u"page 5 of 6\nindia's fastest growing multispeciality clinic & diagnostics chain\n"}]]), ([[{'y1': 1147, 'y0': 1134, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1147, 'y0': 1134, 'x0': 13, 'x1': 1000, 'text': u'e - space building, a-2 wing, 2nd floor, pune nagar road, vadgaonsnet, pune 4014.\n'}]]), ([[{'y1': 1175, 'y0': 1147, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1175, 'y0': 1147, 'x0': 13, 'x1': 1000, 'text': u'o: 1800-267-91910 9191@expressclinics.in\n'}]]), ([[{'y1': 1199, 'y0': 1175, 'x0': 0, 'x1': 133, 'text': u''},
        {'y1': 1199, 'y0': 1175, 'x0': 133, 'x1': 388, 'text': u'e consultations\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 388, 'x1': 512, 'text': u'diagnostics\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 512, 'x1': 650, 'text': u's * healthchecks\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 650, 'x1': 1000, 'text': u'pathology\n'}]]), ([{'y1': 1200, 'y0': 1199, 'x0': 0, 'x1': 1000, 'text': ''}])], [([[{'y1': 283, 'y0': 262, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 283, 'y0': 262, 'x0': 11, 'x1': 1000, 'text': u'haematology report\n'}],
       [{'y1': 326, 'y0': 283, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 326, 'y0': 283, 'x0': 11, 'x1': 1000, 'text': u'test name results\nblood group whole blood by slide method\nunits\nnormal range\n'}],
       [{'y1': 403, 'y0': 326, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 403, 'y0': 326, 'x0': 11, 'x1': 1000, 'text': u"blood group\n'b' rh positive\n"}],
       [{'y1': 716, 'y0': 403, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 716, 'y0': 403, 'x0': 11, 'x1': 1000, 'text': u'**end of report\n'}],
       [{'y1': 1068, 'y0': 716, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1068, 'y0': 716, 'x0': 11, 'x1': 1000, 'text': u'ad by a re eaad b;\ndr. reddy\nin dipatrology, reg ha 384\n'}],
       [{'y1': 1086, 'y0': 1068, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1086, 'y0': 1068, 'x0': 11, 'x1': 1000, 'text': u''}]]), ([[{'y1': 1088, 'y0': 1086, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1088, 'y0': 1086, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1134, 'y0': 1088, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1134, 'y0': 1088, 'x0': 11, 'x1': 1000, 'text': u"page 6 of 6\nindia's fastest growing multispeciality clinic & diagnostics chain\n"}]]), ([[{'y1': 1147, 'y0': 1134, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1147, 'y0': 1134, 'x0': 13, 'x1': 1000, 'text': u'e - space building, a-2 wing, 2nd floor, pune nagar road, vadgaonsnet, pune 4014.\n'}]]), ([[{'y1': 1175, 'y0': 1147, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1175, 'y0': 1147, 'x0': 13, 'x1': 1000, 'text': u'o: 1800-267-91910 9191@expressclinics.in\n'}]]), ([[{'y1': 1199, 'y0': 1175, 'x0': 0, 'x1': 133, 'text': u''},
        {'y1': 1199, 'y0': 1175, 'x0': 133, 'x1': 388, 'text': u'e consultations\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 388, 'x1': 512, 'text': u'diagnostics\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 512, 'x1': 650, 'text': u's * healthchecks\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 650, 'x1': 1000, 'text': u'pathology\n'}]]), ([{'y1': 1200, 'y0': 1199, 'x0': 0, 'x1': 1000, 'text': ''}])], [([[{'y1': 283, 'y0': 262, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 283, 'y0': 262, 'x0': 11, 'x1': 1000, 'text': u'lipid profile report\n'}],
       [{'y1': 326, 'y0': 283, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 326, 'y0': 283, 'x0': 11, 'x1': 1000, 'text': u'test name\ntotal lipid profile\nresults\nunits\nnormal range\n'}],
       [{'y1': 412, 'y0': 326, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 412, 'y0': 326, 'x0': 11, 'x1': 1000, 'text': u'cholesterol\n123.0\nmg/dl\ndesirable - less than : 200\nmg/dl\nborderline high - 200 to\n239 mg/dl\nhigh > 230 mg/di\n'}],
       [{'y1': 496, 'y0': 412, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 496, 'y0': 412, 'x0': 11, 'x1': 1000, 'text': u'triglycerides\n215.0\nmg/dl\nnormalup to 150\nhigh: 150 to 199\nhypertriglyceidemic: 200 to\n499\nvery high: >499\n'}]]), ([[{'y1': 499, 'y0': 496, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 499, 'y0': 496, 'x0': 20, 'x1': 244, 'text': ''},
        {'y1': 499, 'y0': 496, 'x0': 244, 'x1': 502, 'text': ''},
        {'y1': 499, 'y0': 496, 'x0': 502, 'x1': 692, 'text': ''},
        {'y1': 499, 'y0': 496, 'x0': 692, 'x1': 1000, 'text': u''}],
       [{'y1': 601, 'y0': 499, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 601, 'y0': 499, 'x0': 20, 'x1': 244, 'text': u'sr. hdl\n'},
        {'y1': 601, 'y0': 499, 'x0': 244, 'x1': 502, 'text': u'31.0\n'},
        {'y1': 601, 'y0': 499, 'x0': 502, 'x1': 692, 'text': u'mg/dl\n'},
        {'y1': 601, 'y0': 499, 'x0': 692, 'x1': 1000, 'text': u'negative risk factor for\nheart disease: > 60\nborderline needs follow up:\n40 to 59\nmajor risk factor for heart\ndisease: < 40\n'}],
       [{'y1': 624, 'y0': 601, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 624, 'y0': 601, 'x0': 20, 'x1': 244, 'text': u'sr.ldl\n'},
        {'y1': 624, 'y0': 601, 'x0': 244, 'x1': 502, 'text': u'49\n'},
        {'y1': 624, 'y0': 601, 'x0': 502, 'x1': 692, 'text': u'maldi\n'},
        {'y1': 624, 'y0': 601, 'x0': 692, 'x1': 1000, 'text': u'60 - 150\n'}],
       [{'y1': 643, 'y0': 624, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 643, 'y0': 624, 'x0': 20, 'x1': 244, 'text': u'sr.vldl\n'},
        {'y1': 643, 'y0': 624, 'x0': 244, 'x1': 502, 'text': u'43\n'},
        {'y1': 643, 'y0': 624, 'x0': 502, 'x1': 692, 'text': u'mg/dl\n'},
        {'y1': 643, 'y0': 624, 'x0': 692, 'x1': 1000, 'text': u'5-40\n'}]]), ([[{'y1': 647, 'y0': 643, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 647, 'y0': 643, 'x0': 20, 'x1': 246, 'text': u''},
        {'y1': 647, 'y0': 643, 'x0': 246, 'x1': 502, 'text': u''},
        {'y1': 647, 'y0': 643, 'x0': 502, 'x1': 692, 'text': u''},
        {'y1': 647, 'y0': 643, 'x0': 692, 'x1': 1000, 'text': u''}],
       [{'y1': 665, 'y0': 647, 'x0': 0, 'x1': 20, 'text': ''},
        {'y1': 665, 'y0': 647, 'x0': 20, 'x1': 246, 'text': u'tc hdl\n'},
        {'y1': 665, 'y0': 647, 'x0': 246, 'x1': 502, 'text': u'3, 97\n'},
        {'y1': 665, 'y0': 647, 'x0': 502, 'x1': 692, 'text': u'mg/di\n'},
        {'y1': 665, 'y0': 647, 'x0': 692, 'x1': 1000, 'text': u''}]]), ([[{'y1': 668, 'y0': 665, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 668, 'y0': 665, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 698, 'y0': 668, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 698, 'y0': 668, 'x0': 11, 'x1': 1000, 'text': u'ldl / hdl\n1.58\nmg/dl\n1.5 - 3.5\n'}],
       [{'y1': 837, 'y0': 698, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 837, 'y0': 698, 'x0': 11, 'x1': 1000, 'text': u'please correlate clinically\n'}],
       [{'y1': 1068, 'y0': 837, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1068, 'y0': 837, 'x0': 11, 'x1': 1000, 'text': u'fierified by a re eased b;\ndrreddy\nin dipatrology, reg ta, 384\n'}],
       [{'y1': 1086, 'y0': 1068, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1086, 'y0': 1068, 'x0': 11, 'x1': 1000, 'text': u''}]]), ([[{'y1': 1088, 'y0': 1086, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1088, 'y0': 1086, 'x0': 11, 'x1': 1000, 'text': u''}],
       [{'y1': 1134, 'y0': 1088, 'x0': 0, 'x1': 11, 'text': ''},
        {'y1': 1134, 'y0': 1088, 'x0': 11, 'x1': 1000, 'text': u"page 3 of 6\nindia's fastest growing multispeciality clinic & diagnostics chain\n"}]]), ([[{'y1': 1147, 'y0': 1134, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1147, 'y0': 1134, 'x0': 13, 'x1': 1000, 'text': u'e - space building, a-2 wing, 2nd floor, pune nagar road, vadgaonsnet, pune 4014.\n'}]]), ([[{'y1': 1175, 'y0': 1147, 'x0': 0, 'x1': 13, 'text': ''},
        {'y1': 1175, 'y0': 1147, 'x0': 13, 'x1': 1000, 'text': u'o: 1800-267-91910 9191@expressclinics.in\n'}]]), ([[{'y1': 1199, 'y0': 1175, 'x0': 0, 'x1': 133, 'text': u''},
        {'y1': 1199, 'y0': 1175, 'x0': 133, 'x1': 388, 'text': u'e consultations\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 388, 'x1': 512, 'text': u'diagnostics\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 512, 'x1': 650, 'text': u's * healthchecks\n'},
        {'y1': 1199, 'y0': 1175, 'x0': 650, 'x1': 1000, 'text': u'pathology\n'}]]), ([{'y1': 1200, 'y0': 1199, 'x0': 0, 'x1': 1000, 'text': ''}])]]




def customer_data(name_data):
    customer_info = []
    for page in name_data:
        for primary_segment in page:
            for row in primary_segment:
                for column in row:
                    if 'patient name' in column['text']:
                        contents = column['text'].split('\n')
                        for content in contents:
                            customer_info.extend(re.findall(r'(patient name\s*:\s*\w*\s*\w*)',content))
                            customer_info.extend(re.findall(r'(gender\s*:\s*\w*\s*)',content))
                            customer_info.extend(re.findall(r'(age\s*:\s*\d+\.?\d*)',content))
                    if len(customer_info) >= 3:
                        break
                if len(customer_info) >= 3:
                        break
            if len(customer_info) >= 3:
                        break

    return customer_info




def test_data_part(test_data):
    test_rows = []
    for page in range(len(test_data)):
        test_row_page= []
        for primary_segment in test_data[page]: 
            for row in range(len(primary_segment)):
                for column in primary_segment[row]:
                    if len(primary_segment) > 1: 
                        test_row_page.append(primary_segment[row])
                    if type(column) is dict and column['text'].startswith('please correlate'):
                        break
                if type(column) is dict and column['text'].startswith('please correlate'):
                    break
            if type(column) is dict and column['text'].startswith('please correlate'):
                break
        test_rows.append(test_row_page)
    return test_rows


def info_retrieval(name_flag,unit_flag,value_flag,column_contents,test_dict,layout):
    for content in column_contents:
        if content is u'' or content is ' ':
            del content
        else:
            name_found = test_name_regex.search(content)
            if name_found and 'test name' not in content and ':' not in content:
                if name_flag == False:
                    test_dict['name'] = content
                    name_flag = True
            value_found = test_value_regex.search(content)
            if value_found  and '<' not in content and '>' not in content and '-' not in content and ':' not in content:
                if '>' not in content and '<' not in content:
                    if value_flag == False:
                        test_dict['value'] = content
                        value_flag = True

            if layout == 1:
                range_found = refer_range_1_regex.search(content)
                range_found_2 = refer_range_regex.search(content)
                if range_found or range_found_2 and '-' in content and '/' not in content:
                    test_dict['ref_range'] = content

            unit_found = test_unit_regex.search(content)
            if unit_found:
                if unit_flag == False:
                    test_dict['unit'] = content 
                    unit_flag = True 
    return test_dict,name_flag,unit_flag,value_flag



def layout_1_retrieval(row,test_row_page):
    layout = 1
    test_list = []
    for row_index in range(test_row_page.index(row) + 1 ,len(test_row_page)):
        test_dict = {'name':'','value':0,'unit':'','ref_range':''}
        name_flag = False
        unit_flag = False
        value_flag = False
        for column in test_row_page[row_index]:
            if page_breaker in column['text'] or 'end of report' in column['text']:
                break

            else:
                column_contents = column['text'].split('\n')
                test_dict,name_flag ,unit_flag,value_flag= info_retrieval(name_flag,unit_flag,value_flag,column_contents,test_dict,layout)
        if test_dict not in test_list:
            test_list.append(test_dict)
        if page_breaker in column['text'] or 'end of report' in column['text']:
            break
    return test_list




def pathology_physical_tests(row,test_row_page):
    found = False
    test_list = []
    for row_index in range(test_row_page.index(row),len(test_row_page)):
        test_dict = test_dict = {'name':'','value':0,'unit':'','ref_range':''}
        for column in test_row_page[row_index]:
            if 'urine' in column['text'] or 'routine-urine' in column['text']:
                found = True
                break
            if page_breaker in column['text'] or 'end of report' in column['text']:
                found = False
                break
            if found == True:
                column_contents = column['text'].split('\n')
                for content in column_contents:
                    if content == '' or content == u'' or content == ' ':
                        del content

                if len(column_contents) >=1:
                    test_dict['name'] = column_contents[0]
                if len(column_contents) >=2:
                    test_dict['value'] = column_contents[1]
                if len(column_contents) ==3:
                    test_dict['ref_range'] = column_contents[2]
                if len(column_contents) >=3:
                    test_dict['unit'] = column_contents[2]
                    test_dict['ref_range'] = column_contents[3]
        if test_dict not in test_list:
            test_list.append(test_dict)
    return test_list





def test_row_process(test_data):
    total_tests = []
    test_rows = test_data_part(test_data)
    for test_row_page in test_rows:
        next_page = False
        for row in test_row_page:
            start = False
            for column in row:
                if test_start  in column['text']:
                    start = True
                
                if start == True :
                    # if layout_identifier_1 in  row[len(row)-1]['text'] or layout_identifier_1 in  row[len(row)-2]['text'] or layout_identifier_1 in  row[len(row)-3]['text']:
                    test_list_1= layout_1_retrieval(row,test_row_page)
                    if 'urine' in column['text'] or 'routine-urine' in column['text']:
                        physical_tests = pathology_physical_tests(row,test_row_page)
                    if test_list_1 not in total_tests:
                        total_tests.append(test_list_1)
                    next_page = True
                    break
                    

            if page_breaker in column['text'] or next_page == True:
                break
    return total_tests,physical_tests





test_start = 'test name'
page_breaker= 'please correlate'

test_name_regex = re.compile(r'([a-z]+\-?\s*)+(\w+|\W+)?')
test_value_regex = re.compile(r'^[0-9]*\.?[0-9]*$|nil')
refer_range_1_regex = re.compile(r'((male:?)(female:?)\d*[\.]?\d*)\-(\d*[\.]?\d*)|[\W*\s*\d+]')
test_unit_regex= re.compile(r'[[a-z]*]|\W*/[a-z]*|%')
refer_range_regex = re.compile(r'\>*\<*\s*\d+|nil\sin\sadults')
refer_range_2_regex = re.compile(r'((male:\s*\d+)?(female:\s*\d+)?(adult\s*\d+)?\d+[\.]?\d*)\-(\d*[\.]?\d*)|[\W*\s*\d+]')




test_series,physical_tests = test_row_process(test_data)

for j in test_series:
    for k in j:
        print(k)
        print('\n')
        print('\n')
for x in physical_tests:
    print(x)
    print('\n')
    print('\n')




# print(physical_tests)
customer_info = customer_data(name_data)
print(customer_info)