import psycopg2  # Biblioteca para conexão com PostgreSQL

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime

# Configurações do banco de dados
DB_PARAMS = {
    'dbname': 'Nome_do_seu_banco_de_dados',
    'user': 'postgres',
    'password': 'sua_senha_do_Postgree',
    'host': 'Seu_IP_Ou_seu_host_do_Postgree',
    'port': '5432'
}

# Função para acrescentar informações nas colunas
def save_to_db(nome_do_operador,turno,maquina,ciclo_maximo,ciclo_minimo,numero_cavidades,ciclo_1,ciclo_2,ciclo_3,ciclo_4,cavidades_funcionando_ciclo_1,cavidades_funcionando_ciclo_2,cavidades_funcionando_ciclo_3,cavidades_funcionando_ciclo_4,ciclo_5,ciclo_6,ciclo_7,ciclo_8,cavidades_funcionando_ciclo_5,cavidades_funcionando_ciclo_6,cavidades_funcionando_ciclo_7,cavidades_funcionando_ciclo_8,produto_produzido,quantidade_produzida,data_da_inspecao):
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        
        # Inserir dados na tabela
        cursor.execute("INSERT INTO Nome_do_seu_banco_de_dados (nome_do_operador, turno, maquina, ciclo_maximo, ciclo_minimo, numero_cavidades,ciclo_1,ciclo_2,ciclo_3,ciclo_4,cavidades_funcionando_ciclo_1,cavidades_funcionando_ciclo_2,cavidades_funcionando_ciclo_3,cavidades_funcionando_ciclo_4,ciclo_5,ciclo_6,ciclo_7,ciclo_8,cavidades_funcionando_ciclo_5,cavidades_funcionando_ciclo_6,cavidades_funcionando_ciclo_7,cavidades_funcionando_ciclo_8,produto_produzido,quantidade_produzida,data_da_inspecao) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nome_do_operador, turno, maquina, ciclo_maximo, ciclo_minimo, numero_cavidades,ciclo_1,ciclo_2,ciclo_3,ciclo_4,cavidades_funcionando_ciclo_1,cavidades_funcionando_ciclo_2,cavidades_funcionando_ciclo_3,cavidades_funcionando_ciclo_4,ciclo_5,ciclo_6,ciclo_7,ciclo_8,cavidades_funcionando_ciclo_5,cavidades_funcionando_ciclo_6,cavidades_funcionando_ciclo_7,cavidades_funcionando_ciclo_8,produto_produzido,quantidade_produzida,data_da_inspecao))
        
        # Confirmar as alterações
        conn.commit()
        
        # Fechar a conexão
        cursor.close()
        conn.close()
    except:
        pass
#****************************************************************************************

today_date = datetime.now().strftime("%d/%m/%Y")


class QuestionScreen1(Screen):
    def __init__(self, **kwargs):
        super(QuestionScreen1,self).__init__(**kwargs)
        
        # Primeira Tela ********************************************************************************************************************************
        # Cria um layout FloatLayout para o conteúdo da tela
        layout = FloatLayout()
        
        # Adiciona a imagem ao canto superior esquerdo
        #img = Image(source='FOTO DE PERFIL.png', 
         #           size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.02, 'y': 0.82})
        #layout.add_widget(img)
        
        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Nome do operador:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto1 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto1)

        # Adiciona uma etiqueta com a segunda pergunta - Data
        question_label_date = Label(text="Data do preenchimento:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.7})
        layout.add_widget(question_label_date)

        # Adiciona uma caixa de texto para o usuário inserir a data
        self.answer_input_date_minha_data = TextInput(text= today_date, size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.6},hint_text_color=(0, 0, 0, 1),foreground_color=(0, 0, 0, 1))
        layout.add_widget(self.answer_input_date_minha_data)

        # Adiciona uma etiqueta com a terceira pergunta - Número da Máquina
        question_label_machine = Label(text="Turno:", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.5})
        layout.add_widget(question_label_machine)

        # Adiciona uma caixa de texto para o usuário inserir o número da máquina
        self.answer_input_machine_texto2 = TextInput(hint_text="Digite seu turno. Ex: MANHÃ = 1, TARDE = 2 e NOITE = 3 ", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.4})
        layout.add_widget(self.answer_input_machine_texto2)

        # Adiciona uma etiqueta com a quarta pergunta - Número da Máquina
        question_label_machine = Label(text="Máquina", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.3})
        layout.add_widget(question_label_machine)

        # Adiciona uma caixa de texto para o usuário inserir o número da máquina
        self.answer_input_machine_texto3 = TextInput(hint_text="Digite o número da máquina: ", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.4, 'y': 0.2})
        layout.add_widget(self.answer_input_machine_texto3)

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo máximo:", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto4 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto4)

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo minimo:", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.7})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto5 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.6})
        layout.add_widget(self.answer_input_name_texto5)



        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite número de cavidades:", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.5})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto6 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.4})
        layout.add_widget(self.answer_input_name_texto6)




        # Adiciona um botão para prosseguir para a próxima tela
        proceed_button = Button(text="Prosseguir", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.44, 'y': 0.05})
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(proceed_button)
        
        self.add_widget(layout)
    

    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):
        self.manager.current = 'question2'


#Segunda tela *****************************************************************************************************************************************
class QuestionScreen2(Screen):
    def __init__(self, **kwargs):
        super(QuestionScreen2,self).__init__(**kwargs)
        
        

        # Cria um layout FloatLayout para o conteúdo da tela, se quero que meu conteudo fique um embaixo do outro ou um do lado do outro
        layout = FloatLayout()
        #-------------------------------------------------------


        # Adiciona a imagem ao canto superior esquerdo
        #img = Image(source='FOTO DE PERFIL.png', 
                    #size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.02, 'y': 0.82})
        #layout.add_widget(img)
        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 1", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto7 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto7)

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 2", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.7})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto8 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.6})
        layout.add_widget(self.answer_input_name_texto8)        


        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 3", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.5})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto9 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.4})
        layout.add_widget(self.answer_input_name_texto9)        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 4", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.3})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto10 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.2})
        layout.add_widget(self.answer_input_name_texto10)   
        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 1", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto11 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto11)

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 2", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.7})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto12 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.6})
        layout.add_widget(self.answer_input_name_texto12)        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 3", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.5})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto13 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.4})
        layout.add_widget(self.answer_input_name_texto13)        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 4", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.3})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto14 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.2})
        layout.add_widget(self.answer_input_name_texto14)        
#----------------------------------------------------------------------

        # Adiciona um botão para prosseguir para a próxima tela
        proceed_button = Button(text="Prosseguir", size_hint=(None, None), size=(105, 50), pos_hint={'center_x': 0.92, 'y': 0.093})
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(proceed_button)
        
        # Adiciona um botão para voltar para a tela anterior
        back_button = Button(text="Voltar", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.080, 'y': 0.090})
        back_button.bind(on_press=self.go_to_previous_screen)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):
        self.manager.current = 'question3'
    
    # Função chamada quando o botão "Voltar" é pressionado
    def go_to_previous_screen(self, instance):
        self.manager.current = 'question1'

#Terceira tela *****************************************************************************************************************************************
        
# Criação pagina 3
class QuestionScreen3(Screen):
    def __init__(self, **kwargs):
        super(QuestionScreen3,self).__init__(**kwargs)
        
        

        # Cria um layout FloatLayout para o conteúdo da tela, se quero que meu conteudo fique um embaixo do outro ou um do lado do outro
        layout = FloatLayout()
        #-------------------------------------------------------


        # Adiciona a imagem ao canto superior esquerdo
        #img = Image(source='FOTO DE PERFIL.png', 
                  #  size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.02, 'y': 0.82})
        #layout.add_widget(img)
        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 5", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto15 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto15)

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 6", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.7})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto16 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.6})
        layout.add_widget(self.answer_input_name_texto16)        


        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 7", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.5})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto17 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.4})
        layout.add_widget(self.answer_input_name_texto17)        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="Digite o ciclo 8", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.2, 'y': 0.3})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto18 = TextInput(hint_text="Digite em segundos", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.2, 'y': 0.2})
        layout.add_widget(self.answer_input_name_texto18)   
        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 5", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.9})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto19 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.8})
        layout.add_widget(self.answer_input_name_texto19)

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 6", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.7})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto20 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.6})
        layout.add_widget(self.answer_input_name_texto20)        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 7", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.5})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto21 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.4})
        layout.add_widget(self.answer_input_name_texto21)        

        # Adiciona uma etiqueta com a primeira pergunta
        question_label_name = Label(text="N° de cavidades funcionando ciclo 8", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.6, 'y': 0.3})
        layout.add_widget(question_label_name)

        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_name_texto22 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.6, 'y': 0.2})
        layout.add_widget(self.answer_input_name_texto22)        


        # Adiciona um botão para prosseguir para a próxima tela
        proceed_button = Button(text="Prosseguir", size_hint=(None, None), size=(105, 50), pos_hint={'center_x': 0.92, 'y': 0.093})
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(proceed_button)
        
        # Adiciona um botão para voltar para a tela anterior
        back_button = Button(text="Voltar", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.080, 'y': 0.090})
        back_button.bind(on_press=self.go_to_previous_screen)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):
        self.manager.current = 'question4'
    
    # Função chamada quando o botão "Voltar" é pressionado
    def go_to_previous_screen(self, instance):
        self.manager.current = 'question2'




#****************************************************************************************** Começa a criação da 4 pagina
class QuestionScreen4(Screen):
    def __init__(self, **kwargs):
        super(QuestionScreen4,self).__init__(**kwargs)
        
        # Cria um layout FloatLayout para o conteúdo da tela
        layout = FloatLayout()
        
        # Adiciona a imagem ao canto superior esquerdo
        #img = Image(source='FOTO DE PERFIL.png', 
                   # size_hint=(None, None), size=(100, 100), pos_hint={'x': 0.02, 'y': 0.82})
        #layout.add_widget(img)
        
        # Adiciona uma etiqueta com a terceira pergunta
        question_label = Label(text="Produto produzido", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.1, 'y': 0.7})
        layout.add_widget(question_label)
        
        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_texto23 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.1, 'y': 0.6})
        layout.add_widget(self.answer_input_texto23)


        # Adiciona uma etiqueta com a terceira pergunta
        question_label = Label(text="Quatidade produzida", size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.1, 'y': 0.5})
        layout.add_widget(question_label)
        
        # Adiciona uma caixa de texto para o usuário inserir a resposta
        self.answer_input_texto24 = TextInput(hint_text="Digite aqui", size_hint=(None, None), size=(300, 50), pos_hint={'x': 0.1, 'y': 0.4})
        layout.add_widget(self.answer_input_texto24)



       
        # Adiciona um botão para prosseguir para a próxima tela (ou voltar para a tela anterior)
        proceed_button = Button(text="Finalizar", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.1})
        proceed_button.bind(on_press=self.go_to_next_screen)
        layout.add_widget(proceed_button)
        
        # Adiciona um botão para voltar para a tela anterior
        back_button = Button(text="Voltar", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.2})
        back_button.bind(on_press=self.go_to_previous_screen)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    # Função chamada quando o botão "Prosseguir" é pressionado
    def go_to_next_screen(self, instance):

        screen1 = self.manager.get_screen('question1')

        screenturno = self.manager.get_screen('question1')

        screenmaquina = self.manager.get_screen('question1')

        screenciclo_maximo = self.manager.get_screen('question1')

        screenciclo_minimo = self.manager.get_screen('question1')

        screennumero_cavidades = self.manager.get_screen('question1')

        screen_data = self.manager.get_screen('question1')
        #---------------------------------------------------------------------
        # Ciclos pagina 2
        screen_ciclo1 = self.manager.get_screen('question2')
        screen_ciclo2 = self.manager.get_screen('question2')
        screen_ciclo3 = self.manager.get_screen('question2')
        screen_ciclo4 = self.manager.get_screen('question2')
        #---------------------------------------------------
        screen_cavidades_funcionando_ciclo_1 = self.manager.get_screen('question2')
        screen_cavidades_funcionando_ciclo_2 = self.manager.get_screen('question2')
        screen_cavidades_funcionando_ciclo_3 = self.manager.get_screen('question2')
        screen_cavidades_funcionando_ciclo_4 = self.manager.get_screen('question2')
        #---------------------------------------------------------------------
        # Ciclos pagina 3
        screen_ciclo5 = self.manager.get_screen('question3')
        screen_ciclo6 = self.manager.get_screen('question3')
        screen_ciclo7 = self.manager.get_screen('question3')
        screen_ciclo8 = self.manager.get_screen('question3')
        #---------------------------------------------------
        screen_cavidades_funcionando_ciclo_5 = self.manager.get_screen('question3')
        screen_cavidades_funcionando_ciclo_6 = self.manager.get_screen('question3')
        screen_cavidades_funcionando_ciclo_7 = self.manager.get_screen('question3')
        screen_cavidades_funcionando_ciclo_8 = self.manager.get_screen('question3')
        #*******************************************
        # Pagina 4
        screen_produto_produzido = self.manager.get_screen('question4')
        screen_quatidade_produzida = self.manager.get_screen('question4')

        #---------------------------------------------------------------------
        # Coletando os textos

        nome_do_operador = screen1.answer_input_name_texto1.text

        turno = screenturno.answer_input_machine_texto2.text
        
        maquina = screenmaquina.answer_input_machine_texto3.text

        ciclo_maximo = screenciclo_maximo.answer_input_name_texto4.text

        ciclo_minimo = screenciclo_minimo.answer_input_name_texto5.text

        numero_cavidades = screennumero_cavidades.answer_input_name_texto6.text

        data_da_inspecao = screen_data.answer_input_date_minha_data.text
        # Ciclos pagina 2-------------------------------------------------
        ciclo_1 = screen_ciclo1.answer_input_name_texto7.text
        ciclo_2 = screen_ciclo2.answer_input_name_texto8.text
        ciclo_3 = screen_ciclo3.answer_input_name_texto9.text
        ciclo_4 = screen_ciclo4.answer_input_name_texto10.text
        #----------------------------------------------------
        # Cavidades pagina 2
        cavidades_funcionando_ciclo_1 = screen_cavidades_funcionando_ciclo_1.answer_input_name_texto11.text
        cavidades_funcionando_ciclo_2 = screen_cavidades_funcionando_ciclo_2.answer_input_name_texto12.text
        cavidades_funcionando_ciclo_3 = screen_cavidades_funcionando_ciclo_3.answer_input_name_texto13.text
        cavidades_funcionando_ciclo_4 = screen_cavidades_funcionando_ciclo_4.answer_input_name_texto14.text
        #------------------------------------------ Pagina 3


        # Ciclos pagina 3
        ciclo_5 = screen_ciclo5.answer_input_name_texto15.text
        ciclo_6 = screen_ciclo6.answer_input_name_texto16.text
        ciclo_7 = screen_ciclo7.answer_input_name_texto17.text
        ciclo_8 = screen_ciclo8.answer_input_name_texto18.text
        #----------------------------------------------------
        # Cavidades pagina 3
        cavidades_funcionando_ciclo_5 = screen_cavidades_funcionando_ciclo_5.answer_input_name_texto19.text
        cavidades_funcionando_ciclo_6 = screen_cavidades_funcionando_ciclo_6.answer_input_name_texto20.text
        cavidades_funcionando_ciclo_7 = screen_cavidades_funcionando_ciclo_7.answer_input_name_texto21.text
        cavidades_funcionando_ciclo_8 = screen_cavidades_funcionando_ciclo_8.answer_input_name_texto22.text
        # Pagina 4
        produto_produzido = screen_produto_produzido.answer_input_texto23.text
        quantidade_produzida = screen_quatidade_produzida.answer_input_texto24.text
        screen4 = self.manager.get_screen('question4')

        # -------------------------------------------------------------------
        # Adicionando o Popup de confirmação
        # Criar o layout do Popup
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Deseja salvar os dados?")
        btn_sim = Button(text="Sim", size_hint_y=None, height=50)
        btn_nao = Button(text="Não", size_hint_y=None, height=50)

        layout.add_widget(label)
        layout.add_widget(btn_sim)
        layout.add_widget(btn_nao)

        popup = Popup(title='Confirmação',
                      content=layout,
                      size_hint=(0.75, 0.5))

        # Função para salvar os dados e reiniciar a aplicação
        def salvar_e_reiniciar(instance):
            # Chama a função de salvar dados
            save_to_db(nome_do_operador, turno, maquina, ciclo_maximo, ciclo_minimo, numero_cavidades,
                       ciclo_1, ciclo_2, ciclo_3, ciclo_4,
                       cavidades_funcionando_ciclo_1, cavidades_funcionando_ciclo_2,
                       cavidades_funcionando_ciclo_3, cavidades_funcionando_ciclo_4,
                       ciclo_5, ciclo_6, ciclo_7, ciclo_8,
                       cavidades_funcionando_ciclo_5, cavidades_funcionando_ciclo_6,
                       cavidades_funcionando_ciclo_7, cavidades_funcionando_ciclo_8,
                       produto_produzido, quantidade_produzida,data_da_inspecao)
                # Limpar os campos de entrada
            screen1.answer_input_name_texto1.text = ''
            screenturno.answer_input_machine_texto2.text = ''
            screenmaquina.answer_input_machine_texto3.text = ''
            screenciclo_maximo.answer_input_name_texto4.text = ''
            screenciclo_minimo.answer_input_name_texto5.text = ''
            screennumero_cavidades.answer_input_name_texto6.text = ''
            screen_ciclo1.answer_input_name_texto7.text = ''
            screen_ciclo2.answer_input_name_texto8.text = ''
            screen_ciclo3.answer_input_name_texto9.text = ''
            screen_ciclo4.answer_input_name_texto10.text = ''
            screen_cavidades_funcionando_ciclo_1.answer_input_name_texto11.text = ''
            screen_cavidades_funcionando_ciclo_2.answer_input_name_texto12.text = ''
            screen_cavidades_funcionando_ciclo_3.answer_input_name_texto13.text = ''
            screen_cavidades_funcionando_ciclo_4.answer_input_name_texto14.text = ''
            screen_ciclo5.answer_input_name_texto15.text = ''
            screen_ciclo6.answer_input_name_texto16.text = ''
            screen_ciclo7.answer_input_name_texto17.text = ''
            screen_ciclo8.answer_input_name_texto18.text = ''
            screen_cavidades_funcionando_ciclo_5.answer_input_name_texto19.text = ''
            screen_cavidades_funcionando_ciclo_6.answer_input_name_texto20.text = ''
            screen_cavidades_funcionando_ciclo_7.answer_input_name_texto21.text = ''
            screen_cavidades_funcionando_ciclo_8.answer_input_name_texto22.text = ''
            screen_produto_produzido.answer_input_texto23.text = ''
            screen_quatidade_produzida.answer_input_texto24.text = ''
            #screen_data.answer_input_date_minha_data.text = ''
            # Fechar o popup
            popup.dismiss()

            # Reiniciar o app voltando para a primeira tela
            self.manager.current = 'question1'

        # Função para apenas fechar o popup
        def nao_fazer_nada(instance):
            popup.dismiss()

        # Conectar os botões às funções
        btn_sim.bind(on_press=salvar_e_reiniciar)
        btn_nao.bind(on_press=nao_fazer_nada)

        # Exibir o popup
        popup.open()

        
    
    # Função chamada quando o botão "Voltar" é pressionado
    def go_to_previous_screen(self, instance):
        self.manager.current = 'question3'

class Qualidade(App):
    def build(self):
        sm = ScreenManager()
        # Adiciona as três telas ao gerenciador de telas
        sm.add_widget(QuestionScreen1(name='question1'))
        sm.add_widget(QuestionScreen2(name='question2'))
        sm.add_widget(QuestionScreen3(name='question3'))
        sm.add_widget(QuestionScreen4(name='question4'))        
        return sm

if __name__ == "__main__":
    Qualidade().run()
