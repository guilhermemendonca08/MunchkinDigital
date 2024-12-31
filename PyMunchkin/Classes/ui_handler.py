from PPlay.gameimage import GameImage
from PPlay.window import Window


class UIHandler:
    def __init__(self, mouse):
        self.mouse = mouse
        self.mouse_clicked_state = False

    def detect_choice(self, target_list):
        selection = None
        for target in target_list:
            if self.mouse.is_over_object(target.get_hurtbox()):
                # print(f"I'm over {target}")
                selection = target
            # print("----------------")
            # print(f"checking {target.get_nome()}")

        if self.mouse.is_button_pressed(1) and selection is not None:
            print(f"I picked {selection.get_nome()}")
            return selection

    def mouse_over_card(self, jogadores):
        selection = None
        for jogador in jogadores:
            for carta in jogador.mao:
                if self.mouse.is_over_object(carta.imagem):
                    # resolve carta sobrepostas pegando a última seleção
                    selection = carta
        return selection

    def mouse_over_object(self, objeto):
        if self.mouse.is_over_object(objeto):
            return True
        else:
            return False

    def is_mouse_left_click_pressed(self, freeze_status):
        if freeze_status is False:
            return self.mouse.is_button_pressed(1)
        else:
            return False

    def clicked(self, target, freeze_status):
        if self.mouse_clicked_state and not self.is_mouse_left_click_pressed(
            freeze_status
        ):
            self.mouse_clicked_state = False
            if target:
                return True
            else:
                return False
        self.mouse_clicked_state = self.is_mouse_left_click_pressed(freeze_status)

