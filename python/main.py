import pygame

from buffalo import utils

def main():

    while not utils.end:
        utils.scene.logic()
        utils.scene.update()
        utils.scene.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )
    
if __name__ == "__main__":

    pygame.mixer.init()
    pygame.mixer.pre_init(22050, -16, 4, 512)

    if not utils.init(
            caption='Buffalo Project',
    ):
        print('buffalo.utils failed to initialize')
        pygame.quit()
        exit()

    from menu import Menu

    utils.set_scene( Menu() )

    main()

    pygame.quit()
