import uiScriptLocale

MAIN = "d:/ymir work/ui/logininterface/"

LOCALE_PATH = uiScriptLocale.LOGIN_PATH
SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "bg1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/de/ui/serverlist.sub",
		},
		{
			"name" : "bg2", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : MAIN + "login.sub",
		},

		## ConnectBoard
		{
			"name" : "ConnectBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 208) / 2,
			"y" : (SCREEN_HEIGHT - 410 - 35),
			"width" : 208,
			"height" : 30,

			"children" :
			(
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 15,
					"y" : 0,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
				},
			),
		},

		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : (SCREEN_WIDTH - 682) / 2,
			"y" : (SCREEN_HEIGHT - 550),

			"image" : MAIN + "loginboard/background.png",

			"children" :
			(
				{
					"name" : "username_title",
					"type" : "image",

					"x" : 175,
					"y" : 110,
					"image" : MAIN + "loginboard/text/username.tga",
				},
				{
					"name" : "passwort_title",
					"type" : "image",

					"x" : 175,
					"y" : 205,
					"image" : MAIN + "loginboard/text/passwort.tga",
				},
				{
					"name" : "ID_Input",
					"type" : "image",
					"x" : 120,
					"y" : 140,
					"image" : MAIN + "loginboard/input.tga",
					"children" :
					(
						{
							"name" : "ID_EditLine",
							"type" : "editline",
							"x" : 10, "y" : 15,
							"width" : 200, "height" : 16,
							"input_limit" : 16,
							"enable_codepage" : 0,
						},
					),
				},
				{
					"name" : "PW_Input",
					"type" : "image",
					"x" : 120,
					"y" : 230,
					"image" : MAIN + "loginboard/input.tga",
					"children" :
					(
						{
							"name" : "Password_EditLine",
							"type" : "editline",
							"x" : 10, "y" : 15,
							"width" : 200, "height" : 16,
							"input_limit" : 16,
							"secret_flag" : 1,
							"enable_codepage" : 0,
						},
					),
				},
				{
					"name" : "SelectConnectButton",
					"type" : "button",

					"x" : 635,
					"y" : 15,

					"default_image" : MAIN + "loginboard/button/button_01.png",
					"over_image" : MAIN + "loginboard/button/button_02.png",
					"down_image" : MAIN + "loginboard/button/button_03.png",
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 30,
					"y" : 310,

					"default_image" : MAIN + "button/button_01.png",
					"over_image" : MAIN + "button/button_02.png",
					"down_image" : MAIN + "button/button_03.png",

					"text" : uiScriptLocale.LOGIN_EXIT,
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x" : 170,
					"y" : 310,

					"default_image" : MAIN + "button/button_01.png",
					"over_image" : MAIN + "button/button_02.png",
					"down_image" : MAIN + "button/button_03.png",

					"text" : uiScriptLocale.LOGIN_CONNECT,
				},
				{
					"name" : "LoginSaveButton",
					"type" : "button",

					"x" : 310,
					"y" : 310,

					"default_image" : MAIN + "button/button_01.png",
					"over_image" : MAIN + "button/button_02.png",
					"down_image" : MAIN + "button/button_03.png",

					"text" : uiScriptLocale.LOGIN_SAVE_TEXT,
				},
				
				####################################################################################################
				### Account Saved Area ###
				###########
				### Acc1
				{
					"name" : "Accounts_title",
					"type" : "image",
					"x" : 470,
					"y" : 60,
					"image" : MAIN + "loginboard/text/accounts.png",
				},
				{
					"name" : "Acc1",
					"type" : "image",
					"x" : 472,
					"y" : 95,
					"image" : MAIN + "loginboard/acc_background.png",
					
					"children" :
					(
						{
							"name" : "Acc1_text",
							"type" : "text",
							"x" : 5, "y" : 4,
							"fontname" : "Tahoma:16",
							"text":"Acc1",
						},
						{
							"name" : "Acc1_use",
							"type" : "button",
							"x" : 145,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/hook_01.png",
							"over_image" : MAIN + "loginboard/button/hook_02.png",
							"down_image" : MAIN + "loginboard/button/hook_03.png",
						},
						{
							"name" : "Acc1_del",
							"type" : "button",
							"x" : 165,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/del_01.png",
							"over_image" : MAIN + "loginboard/button/del_02.png",
							"down_image" : MAIN + "loginboard/button/del_03.png",
						},
					),
				},
				###########
				### Acc2
				{
					"name" : "Acc2",
					"type" : "image",
					"x" : 472,
					"y" : 125,
					"image" : MAIN + "loginboard/acc_background.png",
					
					"children" :
					(
						{
							"name" : "Acc2_text",
							"type" : "text",
							"x" : 5, "y" : 4,
							"fontname" : "Tahoma:16",
							"text":"Acc2",
						},
						{
							"name" : "Acc2_use",
							"type" : "button",
							"x" : 145,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/hook_01.png",
							"over_image" : MAIN + "loginboard/button/hook_02.png",
							"down_image" : MAIN + "loginboard/button/hook_03.png",
						},
						{
							"name" : "Acc2_del",
							"type" : "button",
							"x" : 165,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/del_01.png",
							"over_image" : MAIN + "loginboard/button/del_02.png",
							"down_image" : MAIN + "loginboard/button/del_03.png",
						},
					),
				},
				###########
				### Acc3
				{
					"name" : "Acc3",
					"type" : "image",
					"x" : 472,
					"y" : 155,
					"image" : MAIN + "loginboard/acc_background.png",
					
					"children" :
					(
						{
							"name" : "Acc3_text",
							"type" : "text",
							"x" : 5, "y" : 4,
							"fontname" : "Tahoma:16",
							"text":"Acc3",
						},
						{
							"name" : "Acc3_use",
							"type" : "button",
							"x" : 145,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/hook_01.png",
							"over_image" : MAIN + "loginboard/button/hook_02.png",
							"down_image" : MAIN + "loginboard/button/hook_03.png",
						},
						{
							"name" : "Acc3_del",
							"type" : "button",
							"x" : 165,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/del_01.png",
							"over_image" : MAIN + "loginboard/button/del_02.png",
							"down_image" : MAIN + "loginboard/button/del_03.png",
						},
					),
				},
				###########
				### Acc4
				{
					"name" : "Acc4",
					"type" : "image",
					"x" : 472,
					"y" : 185,
					"image" : MAIN + "loginboard/acc_background.png",
					
					"children" :
					(
						{
							"name" : "Acc4_text",
							"type" : "text",
							"x" : 5, "y" : 4,
							"fontname" : "Tahoma:16",
							"text":"Acc4",
						},
						{
							"name" : "Acc4_use",
							"type" : "button",
							"x" : 145,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/hook_01.png",
							"over_image" : MAIN + "loginboard/button/hook_02.png",
							"down_image" : MAIN + "loginboard/button/hook_03.png",
						},
						{
							"name" : "Acc4_del",
							"type" : "button",
							"x" : 165,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/del_01.png",
							"over_image" : MAIN + "loginboard/button/del_02.png",
							"down_image" : MAIN + "loginboard/button/del_03.png",
						},
					),
				},
				###########
				### Acc5
				{
					"name" : "Acc5",
					"type" : "image",
					"x" : 472,
					"y" : 215,
					"image" : MAIN + "loginboard/acc_background.png",
					
					"children" :
					(
						{
							"name" : "Acc5_text",
							"type" : "text",
							"x" : 5, "y" : 4,
							"fontname" : "Tahoma:16",
							"text":"Acc5",
						},
						{
							"name" : "Acc5_use",
							"type" : "button",
							"x" : 145,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/hook_01.png",
							"over_image" : MAIN + "loginboard/button/hook_02.png",
							"down_image" : MAIN + "loginboard/button/hook_03.png",
						},
						{
							"name" : "Acc5_del",
							"type" : "button",
							"x" : 165,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/del_01.png",
							"over_image" : MAIN + "loginboard/button/del_02.png",
							"down_image" : MAIN + "loginboard/button/del_03.png",
						},
					),
				},
				###########
				### Acc6
				{
					"name" : "Acc6",
					"type" : "image",
					"x" : 472,
					"y" : 245,
					"image" : MAIN + "loginboard/acc_background.png",
					
					"children" :
					(
						{
							"name" : "Acc6_text",
							"type" : "text",
							"x" : 5, "y" : 4,
							"fontname" : "Tahoma:16",
							"text":"Acc6",
						},
						{
							"name" : "Acc6_use",
							"type" : "button",
							"x" : 145,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/hook_01.png",
							"over_image" : MAIN + "loginboard/button/hook_02.png",
							"down_image" : MAIN + "loginboard/button/hook_03.png",
						},
						{
							"name" : "Acc6_del",
							"type" : "button",
							"x" : 165,
							"y" : 5,
							"default_image" : MAIN + "loginboard/button/del_01.png",
							"over_image" : MAIN + "loginboard/button/del_02.png",
							"down_image" : MAIN + "loginboard/button/del_03.png",
						},
					),
				},
				####################################################################################################
			),
		},

		## ServerBoard
		{
			"name" : "ServerBoard",
			"type" : "image",

			"x" : 0,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT - 200,
			"width" : 375,
			"height" : SERVER_BOARD_HEIGHT,
			"horizontal_align" : "center",
			"image" : MAIN + "serverselect/background/serverselect_background.png",

			"children" :
			(
				{
					"name" : "server_title",
					"type" : "image",

					"x" : 175,
					"y" : 55,
					"image" : MAIN + "serverselect/title/server_title.png",
				},
				{
					"name" : "channel_title",
					"type" : "image",

					"x" : 345,
					"y" : 55,
					"image" : MAIN + "serverselect/title/channel_title.png",
				},

				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 100,
					"y" : 85,
					"width" : 354,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 100,
					"y" : 86,
					"width" : 355,
					"height" : 0,
					"color" : 0xff111111,
				},

				## Vertical
				{
					"name" : "VerticalLine1",
					"type" : "line",

					"x" : 344,
					"y" : 70,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff777777,
				},
				{
					"name" : "VerticalLine2",
					"type" : "line",

					"x" : 344,
					"y" : 70,
					"width" : 0,
					"height" : SERVER_LIST_HEIGHT + 4,
					"color" : 0xff111111,
				},

				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox2",

					"x" : 100,
					"y" : 102,
					"width" : 232,
					"height" : SERVER_LIST_HEIGHT,

					"item_align" : 1,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",

					"x" : 345,
					"y" : 100,
					"width" : 109,
					"height" : SERVER_LIST_HEIGHT,

					"item_align" : 0,
				},

				## Buttons
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 360,
					"y" : 430,

					"default_image" : MAIN + "button/button_01.png",
					"over_image" : MAIN + "button/button_02.png",
					"down_image" : MAIN + "button/button_03.png",

					"text" : uiScriptLocale.OK,
				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 360,
					"y" : 460,

					"default_image" : MAIN + "button/button_01.png",
					"over_image" : MAIN + "button/button_02.png",
					"down_image" : MAIN + "button/button_03.png",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},

			),

		},
	),
}
