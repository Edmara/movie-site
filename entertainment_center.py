import media
import fresh_tomatoes

new_hope = media.Movie('Star Wars Episódio IV: Uma Nova Esperança',
                        'Storyline',
                        'https://www.barakashop.co.za/media/catalog/product/cache/1/image/650x/040ec09b1e35df139433887a97daa66f/s/t/star_wars_a_new_hope_poster.jpg',
                        'https://www.youtube.com/watch?v=jVrf_bKTjo4')


the_empire_strikes_back = media.Movie('Episódio V - O Império Contra-Ataca',
                     'Storyline',
                     'https://imgc.allpostersimages.com/img/print/u-g-EQRFY0.jpg?w=550&h=550&p=0',
                     'https://www.youtube.com/watch?v=4KnAyxgZ3Vo',)

return_jedi = media.Movie('Episódio VI - O Retorno de Jedi',
                        '',
                        'https://imgc.allpostersimages.com/img/print/u-g-EZYVJ0.jpg?w=550&h=550&p=0',
                        'https://www.youtube.com/watch?v=BT-fVW24-q4')

the_phantom_menace = media.Movie('Episódio I - A Ameaça Fantasma',
                             'Storyline',
                             'https://i.ebayimg.com/images/g/7VMAAOSwcj5ZT~rQ/s-l300.jpg',
                             'https://www.youtube.com/watch?v=JdtZWJyLiz0')

attack_of_the_clones = media.Movie('Episódio II - Ataque dos Clones',
                          'Storyline',
                          'http://crushingkrisis.com/assets/Star_Wars_Episode_II_Attack_of_the_Clones_theatrical_poster-300x442.jpg',
                          'https://www.youtube.com/watch?v=n7DQ9SdjUmg')

revenge_of_sith = media.Movie ('Episódio III - A Vingança dos Sith',
                                 'Storyline',
                                 'https://vignette.wikia.nocookie.net/swfans/images/a/a6/RevengeOfTheSithPoster.jpg/revision/latest/scale-to-width-down/321?cb=20130726070536',
                                 'https://www.youtube.com/watch?v=5UnjrG_N8hU')

movies = [new_hope, the_empire_strikes_back, return_jedi, the_phantom_menace, attack_of_the_clones, revenge_of_sith]
fresh_tomatoes.open_movies_page(movies)

