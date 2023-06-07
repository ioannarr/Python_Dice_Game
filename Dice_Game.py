'''Importamos random con valores del 1 al 6 para asignarle el valor a la tirada'''

import random


class Die:


    def __init__(self):
        self._value = None


    @property
    def value(self):
        return self._value

    '''El metodo usa random para asignar el valor'''
    def roll_dice(self):
        new_value = random.randint(1,6)    
        self._value = new_value
        return new_value


class Player:

    '''El constructor de jugador tiene la agregacion de la clase die '''
    def __init__ (self, die, is_computer=False):
        self._die = die     
        self._is_computer = is_computer
        self._counter = 10
    
    ''' Usamos las properties con get para que no sean usadas por fuera de la clase '''

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    

    '''Contador sube'''
    def increment_counter(self):
        self._counter += 1

    '''Contador a la baja'''
    def decrement_counter(self):
        self._counter -= 1

    """ Aggregacion de la clase Die trayendo el metodo roll_dice"""

    def roll_die(self):
        return  self._die.roll_dice()



class DiceGame:


    def __init__ (self, player, computer):

        self._player = player
        self._computer = computer
    

    def play(self):

        self.print_welcome()

        while True:
            self.jugada()
            game_over = self.check_game_over()
            if game_over == True:
                break


    def jugada(self):

        print('-----------------------------')
        print('Nueva jugada')
        print('-----------------------------')
        input('Tire el Dado: ')
  
        player_value = self._player.roll_die()       
        computer_value = self._player.roll_die()

        self.show_dice_results(self, player_value, computer_values)
      
        """Determinamos el ganador con el valor de la jugada mas grande"""
        if player_value > computer_value:
            self.update_counter(winner=self._player, looser=self._computer)
            print('Player Humano gano la jugada')
        elif player_value < computer_value:
            self.update_counter(winner=self._computer,looser=self._player)
            print("Player Computadora gano la jugada")
        else: 
            print(' Es un empate entre los jugadores')
            self.show_counter()

     

    '''Metodo Estatico'''
    '''Damos la bienvenida'''
    def print_welcome(self):

        print('-----------------------------')
        print('Bienvenido al Juego de Dados')
        print('-----------------------------')


    '''Metodo Estatico'''
    """Mostramos el resultado de las jugadas"""
    def show_dice_results(self, player_value, computer_values):
         
        print('Valor de la jugaga Humano: {player_value}')
        print('Valor de la jugaga Computadora: {computer_value}')


    'Updateamos los contadores'
    def update_counter(self, winner, looser):
        winner.decrement_counter()
        looser.increment_counter()


    '''Modificamos los contadores'''
    def show_counter(self):
        
        print(f'Contador de player1: {self._player.counter}')
        print(f'Contador de computadora: {self._computadora.counter}')


    def check_game_over(self):
        
        if self._player.counter == 0:
            print('Ganador es player ')
            return True
            
        elif self._computer.counter == 0:
            print ('Ganador es la computadora ')
            return True
        
        else:
            return False
    
    def show_game_over(self, winner):
        if winner.is_computer:
            print('Gano la computadpra.')
        elif winner.is_player:
            print('Gano el Humano.')
        
