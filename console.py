#! env bin/python
# codding = utf-8
from collections import namedtuple

cli = {'name': 'root',
       'template': 'Enter command (open,draw, exit)',
       'child': {'child-info': [{'name': 'open',
                                  'template': 'ENTER FILE NAME )',
                                  'child': ""},
                                {'name': 'draw',
                                  'template': 'Enter circle or rectangle',
                                  'child': {'child-info': [{'name': 'circle',
                                                           'template': 'x y R color',
                                                           'child': ""
                                                            },

                                                           {'name': 'rectangle',
                                                           'template': 'x1 y1 x2 y2 color',
                                                           'child': ""}]
                                            },
                                },
                                 {'name': 'exit',
                                  'template': 'Really exit??(yes or no)',
                                  'child': ""}]
                 },
       'test': "hello"
       }

'''{'child-info': [{'name': 'input x',
                                                                              'template': 'x)',
                                                                              'child': ""},
                                                                              {'name': 'input y',
                                                                              'template': 'y',
                                                                              'child': ""},
                                                                                   {'name': 'input r',
                                                                                    'template': 'R',
                                                                                    'child': ""}
                                                                                   ]
                                                               },'''

def user_interface_generator():
    while True:
        command_for_send = []
        # com = input("Input command: ")
        com = input(cli['template'])
        print("enter command %s" % com)
        # print(list(cli['child']['child-info']))
        lst = cli['child']['child-info']
        # print(lst)
        command_for_send.append(com)

        def r(lst, com):
            if lst != {}:
                # print(len(lst))
                for i in lst:
                    if com in i.values():
                        # print(i)
                        if i != {} :
                            # print(i['template'])
                            com1 = input(i['template'])
                            command_for_send.append(com1)
                            # print(i['child'])
                            if i['child'] != "":
                                lst1 = i['child']['child-info']
                                # print('---------------')
                                r(lst1, com1)

        if cli['child'] != "":
            r(lst, com)

        yield command_for_send


        # else:
        #     print('error')
        #     continue
        #def rec(com):
        # while True:
        #     if com in cli:
        #         yield com
        #         # key =
        #         print(cli[com]['cmd'])
        #         break
        #
        #         '''if count == 0:
        #             print(cli[com]['cmd'])
        #             if cli[com]['cmd'] == "":
        #                 break
        #                 yield com
        #             else:
        #                 continue
        #         elif count == 1:
        #             if cli[com]['cmd'][com] == "":
        #                 break
        #                 yield com
        #
        #             else:
        #                 continue'''
        #
        #             #yield com
        #             #print(cli[com]['cmd'][com])
        #             #break
        #         count += 1
        #         # continue
        #     else:
        #         print("Error")
        #         # yield com
        #         continue
                    #rec(com)
        #rec(com)


        '''
                def r(cli):
            if cli['child']['child-info'] != []:
                print(list(cli['child']['child-info']))

                for i in cli['child']['child-info']:
                    if com in i.values():
                        command_for_send.append(com)
                        r()
        '''