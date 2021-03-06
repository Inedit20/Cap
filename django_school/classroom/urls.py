from django.urls import include, path

from .views import classroom, students

urlpatterns = [

    
       path('home_page/', students.home_page.as_view(), name='home_page'),
       path('mots_cles/add/', students.SubjectCreateView.as_view(), name='subject_add'),
       path('domaine/add/', students.DomaineCreateView.as_view(), name='domaine_add'),
       path('type/add/', students.TypeCapteurCreateView.as_view(), name='type_add'),
       path('flyer/', students.FlyerView.as_view(), name='flyer'),
       path('profile_detail/<int:pk_1>/<int:pk_2>/', students.StudentListView.as_view(), name='student_profile'),
       path('collaboration/potentielle/<int:pk_1>/profil_projet/<int:pk_2>/', students.Potentielle_profil.as_view(), name='student_profile_projet'),
       path('expert/<int:pk_1>/', students.expert_annuaire.as_view(), name='annuaire_expert'),
       path('pdf/', students.GeneratePdf.as_view()),
       path('subscribe/', students.subscribe, name = 'subscribe'),
       path('confirmation/<int:pk_1>/<int:pk_2>/<int:pk_3>/<int:notice_id>', students.confirmation_projet, name = 'confirmation_projet'),
       path('confirmation/expert/<int:pk_1>/<int:pk_2>/<int:pk_3>/<int:notice_id>', students.confirmation_expert, name = 'confirmation_expert'),
       path('projet/public/detail/<slug:slug>', students.display_detail_public, name='projet_public'),
       path('projet/public/collaboration/<slug:slug>', students.display_detail_public_coll, name='display_detail_public_coll'),
       path('projet/public/collaboration/actu/<slug:slug>', students.display_detail_public_coll_ac, name='display_detail_public_coll_ac'),
       path('capteur/public/detail/<slug:slug>', students.display_detail_capteur_public, name='capteur_public'),
       path('espace/projet/public/detail/<slug:slug>', students.espace_public, name='espace_public'),
       path('espace/capteur/public/detail/<slug:slug>', students.espace_capteur_public, name='espace_capteur_public'),
       path('boite_a_idees', students.index, name='question_an'),
       path('question/<int:qid>/<slug:qslug>', students.viewquestion),
       path('ask-question', students.askquestion, name='ask_question'),
       path('ajax-answer-question', students.ajaxanswerquestion),
       path('CapMat/', include(([
       path('Accueil/', students.AccueilListView.as_view(), name='first_page'),
       path('Profile/', students.profile_view, name='profile'),
       path('Profile_display/', students.profile, name='profile_dispaly'),
       
       

#Partie 2
#===================================<<<<#Projets >>>>===============================



        path('Projet/', students.HomeView.as_view(), name='lanceur_projet_home'),
        path('resultats_page/<int:pk>/', students.ExpertListView.as_view(), name='collaboration_page'),
        #Mesprojets
        path('Projets/', students.MesProjetsView.as_view(), name='mes_projets'),
        #mettre ?? jour
        path('projet/<int:pk>/', students.QuizUpdateView.as_view(), name='projet_change'),

       #detail projetMesTechnologies_list
        path('projet/detail/<slug:slug>', students.display_detail, name='projet_detail'),








#Partie 3 
#===================================<<<<#Colaborations>>>>===============================


        #collaboration
          path('collaborations/accueil', students.CollobarationListView.as_view(), name='collaborations'),
        #collaboration_potentielle
          path('collaborations/potentielles', students.PotentielleListView.as_view(), name='list_potentielle'),
         #collaboration_actuelle
          path('collaborations/actuelles', students.ActuelleListView.as_view(), name='list_actuelle'),
         #collaboration_contact
          path('collaborations/contact/<int:pk>/', students.sub_projet, name='potentielle_contact'), 
          
          path('chaine_de_Connaissance/<int:pk>/', students.ChaineListView.as_view(), name='chaine'),




#Partie 3 
#===================================<<<<#Technologies>>>>===============================
        #technologies
        path('technologies/Accueil', students.technologieListView.as_view(), name='technologies'),
        #La banque de technologies
        path('Technologies/Accueil/MesTechnologies', students.MesTechnologiesListView, name='MesTechnologies_list'),

        #Capteurs
        path('Capteurs/', students.CapteursView.as_view(), name='capteur_home'),
        path('capteur/ajouter/', students.CapteurCreateView.as_view(), name='capteur_add'),
        path('capteur/<int:pk>/modifier', students.CapteurUpdateView.as_view(), name='capteur_change'),
        path('capteur/<int:pk>/supprimer/', students.CapteurDeleteView.as_view(), name='capteur_delete'),
        path('capteur/detail/<slug:slug>', students.display_detail_capteur, name='capteur_detail'),


#Partie  4
     #Experts
        path('Experts/', students.ExpertsHomeListView.as_view(), name='expert_home'),
        path('Experts/<int:pk_1>/confirmation/<int:pk_2>/', students.sub_createxpert, name='expert_confirmation'),
        path('Collaboration_send/<int:pk_1>/<int:pk_2>/', students.sub_creatcollab, name='sub_creatcollab'),
        path('Experts/Annuaire', students.AnnuaireListView, name='Annuaire'),
        path('Experts/Liste', students.ExpertPotentielleListView.as_view(), name='liste'),
        path('Experts/Favoris/<int:pk_1>/confirmation/<int:pk_2>/', students.favoris, name='favoris'),


        path('free/', students.free, name='free'),




          
        path('equipe/projet/<int:pk>/', students.equipe_definition, name='equipe_projet'),
        path('equipe/projet/change/<int:pk>/', students.equipe_change.as_view(), name='equipe_change'),




      
   

        path('projet/add/', students.QuizCreateView.as_view(), name='projet_add'),
       
        path('projet/<int:pk>/delete/', students.QuizDeleteView.as_view(), name='projet_delete'),
        path('projet/detail/<slug:slug>', students.display_detail, name='projet_detail'),

        path('espace', students.ForumListView, name='forum_list'),
        path('espace/par/<username>/', students.ForumUserListView.as_view(), name='forum-by'),
        path('espace/par/profile/<username>/', students.ProfilUserListView.as_view(), name='forum_by_profile'),
        path('esm/projet/detail/<slug:slug>', students.forum_projet_detail, name='forum_detail'),

        
        #subject 


        #Gestion projet PDF 

        path('projet/pdf/<int:pk>', students.PdfGestionView.as_view(), name='gestionPDF'),

        #Recherche 

        path('expert', students.ExpertsListView, name='experts_list'),
        path('capteur', students.CapteurListView, name='capteurs_list'),
        path('partager/<int:pk>/', students.Publi_projet, name='publi_projet'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('mes_projet/', students.QuizMesView.as_view(), name='projet_list'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
        path('_id??es/', students.BoiteListView, name='boite_list'),
        path('_id??es/form', students.IdeeCreateView.as_view(), name='idee_form'),
        ], 'classroom'), namespace='students')),



#Partie 3 
#===================================<<<<#Boites ?? id??es>>>>===============================
        


]







