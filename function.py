import pygame
import sys
from bullets import Bullet
from alien import Alien
from time import sleep

def check_events(ship,setting,screen,bullets,play_button,states,aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button,mouse_x,mouse_y,states,aliens,ship,setting,screen)
        elif event.type == pygame.KEYDOWN:
            key_down(event,ship,setting,screen,bullets,states,aliens)

        elif event.type == pygame.KEYUP:
            key_up(event,ship)

def check_play_button(play_button,mouse_x,mouse_y,states,aliens,ship,setting,screen):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not states.game_active:
        states.game_active = True
        states.limited_bullets = 3
        aliens.empty()
        ship.ship_centerx()
        creat_aliens(aliens,setting,screen,ship)
        pygame.mouse.set_visible(False)

def start_game(states,aliens,ship,setting,screen):
    states.game_active = True
    states.limited_bullets = 3
    aliens.empty()
    ship.ship_centerx()
    creat_aliens(aliens, setting, screen, ship)
    pygame.mouse.set_visible(False)

def key_down(event,ship,setting,screen,bullets,states,aliens):
    if event.key == pygame.K_RIGHT:
        ship.ship_right = True
    elif event.key == pygame.K_LEFT:
        ship.ship_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        if len(bullets) < setting.maxb:
            new_bullet = Bullet(setting,ship,screen)
            bullets.add(new_bullet)
    elif event.key == pygame.K_p:
        if not states.game_active:
            start_game(states,aliens,ship,setting,screen)


def key_up(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.ship_right = False

    elif event.key == pygame.K_LEFT:
        ship.ship_left = False



def bullet_update(bullets,aliens,states,setting,border):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rt_b.top < 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets,aliens,False,True)
    if collision:
        for aliens in collision.values():
            states.score += setting.alien_score * len(aliens)
            border.prep_image(setting, states)
            check_high_score(states,border,setting)


def line_row_aliens(screen,setting,ship):
    new_alien = Alien(screen, setting)
    line_space = setting.sw - 2 * new_alien.rt_a.width
    line_number = int(line_space / (2 * new_alien.rt_a.width))

    row_space = setting.sh - 3 *  new_alien.rt_a.height - ship.rt_ship.height
    row_number = int(row_space / ( 2 * new_alien.rt_a.height))
    return line_number,row_number

def add_alien(screen,setting,aliens,i,j):
    new_alien = Alien(screen, setting)
    new_alien.rt_a.x = new_alien.rt_a.width + 2 * i * new_alien.rt_a.width
    new_alien.rt_a.y = new_alien.rt_a.height + 2 * j * new_alien.rt_a.height
    aliens.add(new_alien)

def creat_aliens(aliens,setting,screen,ship):
    line_number,row_number =line_row_aliens(screen,setting,ship)
    for i in range(line_number):
        for j in range(row_number):
            add_alien(screen,setting,aliens,i,j)


def blitscreen(setting,screen,ship,bullets,aliens,play_button,states,border):
    screen.fill(setting.cl)
    ship.blitme()
    for i in aliens.sprites():
        i.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not states.game_active:
        play_button.blitme()
    border.blitme()
    pygame.display.flip()


def change_aliens_point(aliens,setting):

    for alien in aliens.sprites():

        if alien.check_edge():
            do_something(aliens, setting)
            break

def do_something(aliens,setting):
    for the_alien in aliens.sprites():
        the_alien.rt_a.y += setting.down_distance
    setting.a_direction *= -1


def update_aliens(ship, aliens, setting, screen, states,bullets,border):

    change_aliens_point(aliens,setting)
    check_aliens_empty(aliens,setting,screen,ship,states,border)
    check_aliens_ship_hit(ship, aliens, setting, screen, states,bullets,border)
    aliens.update()
    aliens_hit_bottom(ship, aliens, setting, screen, states,bullets,border)


def check_aliens_ship_hit(ship,aliens,setting,screen,states,bullets,border):
    if pygame.sprite.spritecollideany(ship,aliens):
        aliens_ship_hit(ship, aliens, setting, screen, states,bullets,border)

def aliens_ship_hit(ship,aliens,setting,screen,states,bullets,border):

    if states.limited_bullets > 0:
        aliens.empty()
        bullets.empty()
        ship.ship_centerx()
        creat_aliens(aliens,setting,screen,ship)
        states.limited_bullets -= 1
        border.prep_ship(states, screen, setting)
        sleep(0.5)

    else:
        setting.init_setting()
        states.reset_game()
        border.prep_ship(states, screen, setting)
        border.prep_level_score(states,setting)
        border.prep_image(setting,states)

        states.game_active = False
        pygame.mouse.set_visible(True)

def aliens_hit_bottom(ship, aliens, setting, screen, states,bullets,border):
    for alien in aliens.sprites():
        if alien.rt_a.bottom >= setting.sh :
            aliens_ship_hit(ship, aliens, setting, screen, states,bullets,border)

def check_aliens_empty(aliens,setting,screen,ship,states,border):
    if len(aliens) == 0:
        creat_aliens(aliens,setting,screen,ship)
        setting.increase_scale()
        states.level +=1
        border.prep_level_score(states,setting)
        sleep(0.5)

def check_high_score(states,border,setting):
    if states.score > states.high_score:
        states.high_score = states.score
        border.prep_high_score(states, setting)

