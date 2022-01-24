#                                                                                                              ================================================================================
#Template for a level list                                                                                     |                   This example is only one individual pressure plate          |
#[Location of the player,[groundtiles to spawn when a level starts],[position of all the coins],[list of all the pressure plates(e.g: [Location(200,200),[[Location(500,500),False,None],[Location(100,100),True,100]]])]]

from gamegrid import Location

level_0 = [Location(20,380),
[[Location(0,400),False,None],[Location(20,400),False,None],[Location(40,400),False,None],[Location(60,400),False,None],[Location(80,400),False,None],[Location(100,400),True,40],[Location(120,400),True,40],[Location(140,400),True,40],[Location(160,400),False,None],[Location(180,400),False,None],[Location(200,400),False,None],[Location(220,400),False,None],[Location(240,400),False,None],[Location(260,400),False,None],[Location(280,400),False,None],[Location(300,400),False,None],[Location(360,390),False,None],[Location(380,390),False,None],[Location(400,390),False,None],[Location(420,390),True,100],[Location(440,390),True,100],[Location(460,390),True,100],[Location(480,390),True,100],[Location(500,390),True,100],[Location(520,390),False,None],[Location(540,390),False,None],[Location(560,390),False,None],[Location(580,390),False,None],[Location(600,390),False,None]],
[Location(260,380)],
[[Location(580,378),[],[],True]]]


level_1 = [Location(20,480),
[[Location(0,500),False,None],[Location(20,500),False,None],[Location(40,500),False,None],[Location(60,500),False,None],[Location(80,500),False,None],[Location(100,500),False,None],[Location(120,500),False,None],[Location(140,500),False,None],[Location(160,500),False,None],[Location(180,500),False,None],[Location(200,500),False,None],[Location(220,500),False,None],[Location(240,500),False,None],[Location(260,500),False,None],[Location(280,500),False,None],[Location(300,500),False,None],[Location(320,500),False,None],[Location(560,300),False,None],[Location(580,300),False,None],[Location(600,300),False,None],[Location(480,460),False,None],[Location(500,460),False,None],[Location(520,460),False,None],[Location(120,380),False,None],[Location(100,380),False,None],[Location(80,380),False,None]],
[Location(500,440),Location(100,360)],
[[Location(320,488),[[Location(380,480),False,None],[Location(400,480),False,None],[Location(420,480),False,None]],[],False],[Location(520,448),[[Location(420,440),False,None],[Location(400,440),False,None],[Location(380,440),False,None],[Location(320,420),False,None],[Location(300,420),False,None],[Location(280,420),False,None],[Location(220,400),False,None],[Location(200,400),False,None],[Location(180,400),False,None]],[[Location(380,480),False,None],[Location(400,480),False,None],[Location(420,480),False,None]],False],[Location(80,368),[[Location(180,360),False,None],[Location(200,360),False,None],[Location(220,360),False,None],[Location(280,340),True,150],[Location(300,340),True,150],[Location(320,340),True,150],[Location(380,320),True,150],[Location(400,320),True,150],[Location(420,320),True,150],[Location(480,300),False,None],[Location(500,300),False,None],[Location(520,300),False,None]],[[Location(420,440),False,None],[Location(400,440),False,None],[Location(380,440),False,None],[Location(320,420),False,None],[Location(300,420),False,None],[Location(280,420),False,None],[Location(220,400),False,None],[Location(200,400),False,None],[Location(180,400),False,None]],False],[Location(580,288),[],[],True]]
]


level_2 = [Location(20,140),
[[Location(0,160),False,None],[Location(20,160),False,None],[Location(40,160),False,None],[Location(60,160),False,None],[Location(80,160),False,None],[Location(100,160),False,None],[Location(120,160),False,None],[Location(160,260),True,50],[Location(180,260),True,50],[Location(100,280),False,None],[Location(80,280),False,None],[Location(60,280),False,None],[Location(400,360),False,None],[Location(420,360),False,None],[Location(440,360),False,None],[Location(100,500),False,None],[Location(120,500),False,None],[Location(140,500),True,100],[Location(160,500),True,100],[Location(180,500),True,100],[Location(200,500),False,None],[Location(220,500),False,None],[Location(240,500),False,None],[Location(140,560),False,None],[Location(160,560),False,None],[Location(180,560),False,None],[Location(500,460),False,None],[Location(480,460),False,None],[Location(460,460),False,None],[Location(440,460),False,None],[Location(360,480),False,None],[Location(340,480),False,None],[Location(320,480),False,None],[Location(300,480),False,None]],
[Location(420,340),Location(320,460)],
[[Location(80,268),[[Location(200,260),False,None],[Location(220,260),False,None],[Location(240,260),False,None],[Location(260,260),False,None],[Location(280,260),False,None],[Location(300,260),False,None]],[],False],[Location(160,548),[],[],True]]
]

level_3 = [Location(20,80),
[[Location(0,100),False,None],[Location(20,100),False,None],[Location(40,100),False,None],[Location(60,100),False,None],[Location(80,100),False,None],[Location(100,100),False,None],[Location(120,100),False,None],[Location(140,100),False,None],[Location(160,100),False,None],[Location(180,100),False,None],[Location(200,100),False,None],[Location(220,100),False,None],[Location(240,100),False,None],[Location(260,100),False,None],[Location(280,100),False,None],[Location(300,100),False,None],[Location(320,100),False,None],[Location(340,100),False,None],[Location(360,100),False,None],[Location(380,100),False,None],[Location(400,100),False,None],[Location(420,100),False,None],[Location(440,100),False,None],[Location(460,100),False,None],[Location(480,100),True,50],[Location(500,100),True,50],[Location(520,100),True,50],[Location(560,80),False,None],[Location(580,80),False,None],[Location(600,80),False,None],[Location(560,500),False,None],[Location(540,500),False,None],[Location(520,500),False,None],[Location(500,500),False,None],[Location(440,500),False,None],[Location(380,500),False,None],[Location(360,500),False,None],[Location(60,440),False,None],[Location(380,300),False,None],[Location(220,220),False,None]],
[Location(440,480),Location(300,240),Location(300,160)],
[[Location(360,488),[[Location(300,480),False,None],[Location(280,480),False,None],[Location(260,480),False,None],[Location(200,460),False,None],[Location(180,460),False,None],[Location(160,460),False,None],[Location(100,440),False,None],[Location(80,440),False,None]],[],False],[Location(60,428),[[Location(140,420),False,None],[Location(180,400),True,100],[Location(220,380),False,None],[Location(260,360),True,100],[Location(300,340),False,None],[Location(340,320),True,100]],[[Location(300,480),False,None],[Location(280,480),False,None],[Location(260,480),False,None],[Location(200,460),False,None],[Location(180,460),False,None],[Location(160,460),False,None]],False],[Location(380,288),[[Location(340,280),True,50],[Location(300,260),False,None],[Location(260,240),True,50]],[],False],[Location(220,208),[[Location(260,200),True,50],[Location(300,180),False,None],[Location(340,160),True,50],[Location(380,140),False,None],[Location(420,120),True,50]],[[Location(200,100),False,None],[Location(220,100),False,None],[Location(240,100),False,None],[Location(260,100),False,None],[Location(280,100),False,None],[Location(300,100),False,None],[Location(320,100),False,None],[Location(340,100),False,None],[Location(360,100),False,None],[Location(380,100),False,None],[Location(400,100),False,None],[Location(420,100),False,None],[Location(440,100),False,None]],False],[Location(580,68),[],[],True]]
]