def couleurs_random():
    global couleurs
    import random
    import requests
    from bs4 import BeautifulSoup
    from random import randint, uniform,random
    liste_rgb = []
    for i in range (0,3):
          num = randint(0, 255)
          liste_rgb.append(num)
    
    liste_rgb = str(liste_rgb)
    liste_rgb = liste_rgb.replace(" ","")
    liste_rgb = liste_rgb.replace("[","")
    liste_rgb = liste_rgb.replace("]","")
    liste_rgb = liste_rgb.replace(",","_")
            
    html = "https://convertingcolors.com/rgb-color-"+liste_rgb +'.html'
    response = requests.get(html)
    soup = BeautifulSoup(response.text, "html.parser")
    compteur = 0
    couleurs = []
    for link in soup.find_all('li'):
        link=link.find('a') 
        compteur += 1
        if compteur > 67:
            link = str(link).split("</span>")
            link = link[1]
            link = link.replace("</a>","")
            link = link.replace("\u2003","")
            couleurs.append(link)    
            if compteur == 73:
                break
    if len(couleurs) < 5 :
        couleurs_random()
    else:
        le_cv()

def le_cv():
    body_ = {}
    body_[1] = '<!DOCTYPE html><html lang="en"><head>'
    
    ############### Fill the following variables
    ### Note the lines 142 to 144 from Body_6 part have to be modified manually : 
    ### '#' are the http link and the icons from https://fontawesome.com/
    ### "class="fa fa-pinterest" can be changed for class="fa fa-facebook for example
    
    Prenom = 'First Name'
    Nom = 'LAST NAME'
    Fonction = 'Data Scientist'
    Address = "3, rue Véron - Paris" 
    Telephone = ' - +33 678 901 234 -'
    email = "my_email_address@gmail.com"
    job = ' Data Scientist'
    title = Prenom +' '+Nom+' / '+job
    intro = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."#An introduction to your profile
    avatar_path = 'C:\\Users\\myname\\'  #src='+ avatar_path+'
    avatar_image_name = 'profile_picture.jpg' #Recommended a 500px x 500px
    social_medias = {'github':'https://github.com/myname.git','linkedin':'https://www.linkedin.com/in/myname/','pinterest':'https://pin.it/mypinterest'}
    
     #EXPERIENCES - NB: Each experience details is an element of the list
    liste_xp_title = ['Xp title 1','Xp title 2','Xp title 3']# Add the experience titles (ex: Sales Representative, Web Developper, etc.). The Xp title 1 is the most recent one
    liste_xp_etp = ['Company 1','Company 2','Company 3']#Add the name of the company you worked for
    liste_xp_content = ['Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',\#Add your job's responsibilities
                        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',\
                        'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']
    liste_xp_date = ['September 2019 to Present','October 2018 to August 2019','May 2016 to September 2017']#Add the start and the end date
    
     #EDUCATION 
    edu_center = ['Education center 1','Education center 2','Education center 3']
    edu_title = ['Master in whatever 1','Master in whatever 2','Master in whatever 3']
    edu_content = ['Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo',\
                'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.',\
                'Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur']
    edu_date = ['From September 2015 to December 2016','From September 2014 to June 2015','From September 2013 to June 2014']
    
     #LIST OF PROGRAMMATION LANGUAGES AND TOOLS
    liste_prog = ['python','html5','css3','bootstrap','mysql','django','mongodb']

     #LIST OF WORKFLOWS
    liste_workflow = ['Neural Network','Django App','Webscraping','Algorythm','Image Recognition System','Prediction models']

     #LIST OF SPEAKING LANGUAGES
    liste_langues = ['PORTUGUESE : Native speaker','ENGLISH : Proficient User','SPANISH : Proficient User']
    
    # LIST OF PROJECTS FOR PORTFOLIO
    liste_projets = ['Business development in East part of France','Online shop','Elearning platform for cooks','Marketing campaign for a famous spririt brand']
    
####################################   
    import base64 
    data_uri = 'data:image/jpeg;base64,'+ base64.b64encode(open(avatar_path + avatar_image_name, 'rb').read()).decode('utf-8')
    
    Links = '<link href="https://fonts.googleapis.com/css?family=Saira+Extra+Condensed:500,700" rel="stylesheet">\
            <link href="https://fonts.googleapis.com/css?family=Muli:400,400i,800,800i" rel="stylesheet">\
            <link rel="stylesheet" href="https://cdn.rawgit.com/konpa/devicon/df6431e323547add1b4cf45992913f15286456d3/devicon.min.css">\
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\
            <link rel="icon" type="image/png" href="https://pngimage.net/wp-content/uploads/2018/06/resume-logo-png-4.png" />'
    
    body_[2]= '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta name="description" content=""><meta name="author" content="">'
        
    body_[3] = '<title>'+title+'</title>'  + Links
    style_css_1 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\css_1.txt", "r")
    style_css_1_defin = ""
    style_css_1_defin += style_css_1.read()
    
    style_css_2 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\css_2.txt", "r")
    style_css_2_defin = ""
    style_css_2_defin += style_css_2.read()
    
    style_css_3 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\css_3.txt", "r")
    style_css_3_defin = ""
    style_css_3_defin += style_css_3.read()
       
    style_css_4 = '.text-primary{color:('+couleurs[0]+')!important}a{color:rgb('+couleurs[3]+')a:active,a:focus,a:hover{color:#824027}'
        
    style_css_5 = '.subheading{text-transform:uppercase;font-weight:500;font-family:"Saira Extra Condensed",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";font-size:1.5rem}'
    
    style_css_6 = '.bg-primary{background-color:rgb('+couleurs[0]+')!important}.text-primary{color:rgb('+couleurs[3]+')!important}a{color:rgb('+couleurs[2]+')a:active,a:focus,a:hover{color:rgb('+couleurs[1]+')}'
    
    body_[4] = '<style>'+ style_css_1_defin + style_css_3_defin + style_css_6 +'</style></head>'
    
    body_[5] = '<body id="page-top"><nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top" id="sideNav">\
        <a class="navbar-brand js-scroll-trigger" href="#page-top"><span class="d-block d-lg-none">'+Prenom+' '+Nom+'</span>\
          <span class="d-none d-lg-block"><img class="img-fluid img-profile rounded-circle mx-auto mb-2" src="'+data_uri+'" alt="">\
          </span></a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\
          <span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent">\
          <ul class="navbar-nav"><li class="nav-item"><a class="nav-link js-scroll-trigger" href="#about">About</a></li>\
            <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#experience">Experience</a></li>\
            <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#education">Education</a></li>\
            <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#skills">Skills</a></li>\
            <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#communication">Communication</a></li>\
            <li class="nav-item"><a class="nav-link js-scroll-trigger" href="#Portfolio">Portfolio</a></li>\
            </ul></div></nav>'
    
    liste_social_script = ''
    for key in social_medias:
        liste_social_script = ''.join((liste_social_script,'<a href="'+social_medias[key]+'"><i class="fa fa-'+key+'></i></a>'))
    
    body_[6] =  '<div class="container-fluid p-0"><section class="resume-section p-3 p-lg-5 d-flex align-items-center" id="about">\
                  <div class="w-100"><h1 class="mb-0">'+ Prenom + '<span class="text-primary">'+' '+ Nom + '</span></h1>\
                  <div class="subheading mb-5">'+ Address + Telephone +' '+ email +'\
                  </div><p class="lead mb-5">'+ intro +'</p><div class="social-icons"><a href="#">\
                  <i class="fa fa-linkedin"></i></a><a href="#"><i class="fa fa-github"></i>\
                  </a><a href="#"><i class="fa fa-pinterest"></i></a>\
                  </a></div></div></section>'

    liste_xp_script = ''
    for i in range(0,len(liste_xp_title)):
        liste_xp_script = ''.join((liste_xp_script,'<div class="resume-item d-flex flex-column flex-md-row justify-content-between mb-5"><div class="resume-content"><h3 class="mb-0">',liste_xp_title[i]))   
        liste_xp_script = ''.join((liste_xp_script,'</h3><div class="subheading mb-3">'+liste_xp_etp[i]))
        liste_xp_script = ''.join((liste_xp_script,'</div><p>'+liste_xp_content[i]))
        liste_xp_script = ''.join((liste_xp_script,'</p></div><div class="resume-date text-md-right"><span class="text-primary">'+liste_xp_date[i]+'</span></div></div>'))

    body_[7] = '<hr class="m-0"><section class="resume-section p-3 p-lg-5 d-flex justify-content-center" id="experience">\
      <div class="w-100"><h2 class="mb-5">Experience</h2>'+liste_xp_script+'</div></section>'

    liste_edu_script = ''
    for i in range(0,len(edu_center)):
        liste_edu_script = ''.join((liste_edu_script,'<div class="resume-item d-flex flex-column flex-md-row justify-content-between mb-5"><div class="resume-content"><h3 class="mb-0">',edu_center[i]))   
        liste_edu_script = ''.join((liste_edu_script,'</h3><div class="subheading mb-3">'+edu_title[i]))
        liste_edu_script = ''.join((liste_edu_script,'</div><p>'+edu_content[i]))
        liste_edu_script = ''.join((liste_edu_script,'</p></div><div class="resume-date text-md-right"><span class="text-primary">'+edu_date[i]+'</span></div></div>'))

    body_[8] = '<hr class="m-0"><section class="resume-section p-3 p-lg-5 d-flex align-items-center" id="education"><div class="w-100">\
        <h2 class="mb-5">Education</h2>'+liste_edu_script+'</div></section>'
    
    liste_prog_script = ''
    for i in liste_prog:
        liste_prog_script = ''.join((liste_prog_script,'<li class="list-inline-item"><i class="devicon-'+i+'-plain"></i></li>'))
    
    liste_workflow_script = ''
    for i in liste_workflow:
        liste_workflow_script = ''.join((liste_workflow_script,'<li><i class="fa-li fa fa-check"></i>'+i+'</li>'))
        
    body_[9] = '<hr class="m-0"><section class="resume-section p-3 p-lg-5 d-flex align-items-center" id="skills">\
      <div class="w-100"><h2 class="mb-5">Skills</h2>\
      <div class="subheading mb-3">Programming Languages &amp; Tools</div>\
        <ul class="list-inline dev-icons">'+ liste_prog_script +'</ul>\
      <div class="subheading mb-3">Workflow</div>\
        <ul class="fa-ul mb-0">'+liste_workflow_script+'</ul></div></section>'

    liste_langues_script = ''
    for i in liste_langues:
        liste_langues_script = ''.join((liste_langues_script,'<li>'+i+'</li>'))
        
    body_[10] = '<hr class="m-0"><section class="resume-section p-3 p-lg-5 d-flex align-items-center" id="communication">\
      <div class="w-100"><h2 class="mb-5">Communication</h2><p>'+liste_langues_script+'</p></div></section>'
    
    liste_projets_script = ''
    for i in liste_projets:
        liste_projets_script = ''.join((liste_projets_script,'<li><i class="fa fa-arrow-circle-right text-warning"></i>'+i+'</li>'))
        
    body_[11] = '<hr class="m-0"><section class="resume-section p-3 p-lg-5 d-flex align-items-center" id="Portfolio">\
      <div class="w-100"><h2 class="mb-5">Portfolio</h2><ul class="fa-ul mb-0">'+liste_projets_script+'</ul></div></section>'
                    
    style_js_1 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\js_1.txt", "r")
    style_js_1_defin = "<script>"
    style_js_1_defin += style_js_1.read()
    style_js_1_defin += "</script>"
    
    style_js_2 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\js_2.txt", "r")
    style_js_2_defin = "<script>"
    style_js_2_defin += style_js_2.read()
    style_js_2_defin += "</script>"
    
    style_js_3 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\js_3.txt", "r")
    style_js_3_defin = "<script>"
    style_js_3_defin += style_js_3.read()
    style_js_3_defin += "</script>"
    
    style_js_4 = open("C:\\Users\\arnau\\OneDrive\\Documentos\\Bootcamp Neoland\\Cours\\Projets\\website generator\\js_4.txt", "r")
    style_js_4_defin = "<script>"
    style_js_4_defin += style_js_4.read()
    style_js_4_defin += "</script>"
    
    body_[99] = '</div>' + style_js_1_defin + style_js_2_defin + style_js_3_defin  +'</body></html>'
    
    site_texte = []
    for key in body_:
        site_texte.append(body_[key])

    Html_file= open(avatar_path+"index.html","w")
    site_texte2 = ''.join(site_texte)
    Html_file.write(str(site_texte2))
    Html_file.close()
    
    import webbrowser
    webbrowser.open(avatar_path + "index.html")

couleurs_random()
