--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 5L (05 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'd\x00\x00k\x00\x00Z\x00\x00e\x00\x00i\x01\x00e\x00\x00i\x02\x00e\x00\x00i\x03\x00f\x03\x00e\x00\x00i\x01\x00e\x00\x00i\x02\x00e\x00\x00i\x02\x00e\x00\x00i\x04\x00f\x04\x00f\x02\x00Z\x05\x00d\x01\x00\x84\x00\x00Z\x06\x00d\x02\x00\x84\x00\x00Z\x07\x00d\x03\x00\x84\x00\x00Z\x08\x00d\x04\x00\x84\x00\x00Z\t\x00d\x05\x00\x84\x00\x00Z\n\x00d\x00\x00S' (70 00 00 00 64 00 00 6B 00 00 5A 00 00 65 00 00 69 01 00 65 00 00 69 02 00 65 00 00 69 03 00 66 03 00 65 00 00 69 01 00 65 00 00 69 02 00 65 00 00 69 02 00 65 00 00 69 04 00 66 04 00 66 02 00 5A 05 00 64 01 00 84 00 00 5A 06 00 64 02 00 84 00 00 5A 07 00 64 03 00 84 00 00 5A 08 00 64 04 00 84 00 00 5A 09 00 64 05 00 84 00 00 5A 0A 00 64 00 00 53)
                 00000000     64 - LOAD_CONST          None
                 00000003     6B - IMPORT_NAME         'obj'
                 00000006     5A - STORE_NAME          'obj'
                 00000009     65 - LOAD_NAME           'obj'
                 0000000C     69 - LOAD_ATTR           'CodeFragmentB'
                 0000000F     65 - LOAD_NAME           'obj'
                 00000012     69 - LOAD_ATTR           'CodeFragmentC'
                 00000015     65 - LOAD_NAME           'obj'
                 00000018     69 - LOAD_ATTR           'TapDataNodeAbility'
                 0000001B     66 - BUILD_TUPLE         r0003
                 0000001E     65 - LOAD_NAME           'obj'
                 00000021     69 - LOAD_ATTR           'CodeFragmentB'
                 00000024     65 - LOAD_NAME           'obj'
                 00000027     69 - LOAD_ATTR           'CodeFragmentC'
                 0000002A     65 - LOAD_NAME           'obj'
                 0000002D     69 - LOAD_ATTR           'CodeFragmentC'
                 00000030     65 - LOAD_NAME           'obj'
                 00000033     69 - LOAD_ATTR           'AnalyzeWeaknessTool'
                 00000036     66 - BUILD_TUPLE         r0004
                 00000039     66 - BUILD_TUPLE         r0002
                 0000003C     5A - STORE_NAME          'Cookbook'
                 0000003F     64 - LOAD_CONST          CODE('CraftRecipe')
                 00000042     84 - MAKE_FUNCTION       r0000
                 00000045     5A - STORE_NAME          'CraftRecipe'
                 00000048     64 - LOAD_CONST          CODE('GetRecipesForWriteCodeLevel')
                 0000004B     84 - MAKE_FUNCTION       r0000
                 0000004E     5A - STORE_NAME          'GetRecipesForWriteCodeLevel'
                 00000051     64 - LOAD_CONST          CODE('GetRecipesForObject')
                 00000054     84 - MAKE_FUNCTION       r0000
                 00000057     5A - STORE_NAME          'GetRecipesForObject'
                 0000005A     64 - LOAD_CONST          CODE('debugTest')
                 0000005D     84 - MAKE_FUNCTION       r0000
                 00000060     5A - STORE_NAME          'debugTest'
                 00000063     64 - LOAD_CONST          CODE('WriteOutCookbook')
                 00000066     84 - MAKE_FUNCTION       r0000
                 00000069     5A - STORE_NAME          'WriteOutCookbook'
                 0000006C     64 - LOAD_CONST          None
                 0000006F     53 - RETURN_VALUE        
             consts:
0000008E         TUPLE: (
00000093             None (4E),
00000094             CODE:
                         argcount:
00000095                     LONG: 0L (00 00 00 00)
                         nlocals:
00000099                     LONG: 6L (06 00 00 00)
                         stacksize:
0000009D                     LONG: 5L (05 00 00 00)
                         flags:
000000A1                     LONG: 71L (47 00 00 00)
                             (OPTIMIZED, NEWLOCALS, VARARGS, NOFREE)
                         code:
000000A5                     STR: 't\x00\x00\x83\x00\x00}\x05\x00x\xb4\x00t\x02\x00D]\xac\x00}\x01\x00t\x04\x00|\x01\x00\x83\x01\x00d\x01\x00\x18t\x04\x00|\x00\x00\x83\x01\x00j\x02\x00o\x89\x00\x01t\x06\x00i\x07\x00d\x02\x00\x83\x01\x00\x01|\x00\x00|\x01\x00t\x04\x00|\x00\x00\x83\x01\x00 j\x02\x00oa\x00\x01d\x03\x00}\x03\x00x5\x00|\x01\x00D]-\x00}\x02\x00t\x06\x00i\n\x00|\x02\x00\x83\x01\x00}\x04\x00|\x03\x00|\x04\x00d\x04\x00\x19\x17}\x03\x00|\x03\x00d\x05\x00\x17}\x03\x00qd\x00Wt\x06\x00i\x07\x00|\x03\x00\x83\x01\x00\x01|\x01\x00t\x04\x00|\x01\x00\x83\x01\x00d\x01\x00\x18\x19Sq\xbc\x00\x01q\x10\x00\x01q\x10\x00Wt\x06\x00i\x07\x00d\x06\x00\x83\x01\x00\x01d\x07\x00Sd\x08\x00S' (D5 00 00 00 74 00 00 83 00 00 7D 05 00 78 B4 00 74 02 00 44 5D AC 00 7D 01 00 74 04 00 7C 01 00 83 01 00 64 01 00 18 74 04 00 7C 00 00 83 01 00 6A 02 00 6F 89 00 01 74 06 00 69 07 00 64 02 00 83 01 00 01 7C 00 00 7C 01 00 74 04 00 7C 00 00 83 01 00 20 6A 02 00 6F 61 00 01 64 03 00 7D 03 00 78 35 00 7C 01 00 44 5D 2D 00 7D 02 00 74 06 00 69 0A 00 7C 02 00 83 01 00 7D 04 00 7C 03 00 7C 04 00 64 04 00 19 17 7D 03 00 7C 03 00 64 05 00 17 7D 03 00 71 64 00 57 74 06 00 69 07 00 7C 03 00 83 01 00 01 7C 01 00 74 04 00 7C 01 00 83 01 00 64 01 00 18 19 53 71 BC 00 01 71 10 00 01 71 10 00 57 74 06 00 69 07 00 64 06 00 83 01 00 01 64 07 00 53 64 08 00 53)
                             00000000     74 - LOAD_GLOBAL         'globals'
                             00000003     83 - CALL_FUNCTION       r0000
                             00000006     7D - STORE_FAST          'globs'
                             00000009     78 - SETUP_LOOP          -> 000000C0
                             0000000C     74 - LOAD_GLOBAL         'Cookbook'
                             0000000F     44 - GET_ITER            
                             00000010     5D - FOR_ITER            -> 000000BF
                             00000013     7D - STORE_FAST          'recipe'
                             00000016     74 - LOAD_GLOBAL         'len'
                             00000019     7C - LOAD_FAST           'recipe'
                             0000001C     83 - CALL_FUNCTION       r0001
                             0000001F     64 - LOAD_CONST          1
                             00000022     18 - BINARY_SUBTRACT     
                             00000023     74 - LOAD_GLOBAL         'len'
                             00000026     7C - LOAD_FAST           'ingredients'
                             00000029     83 - CALL_FUNCTION       r0001
                             0000002C     6A - COMPARE_OP          "=="
                             0000002F     6F - JUMP_IF_FALSE       -> 000000BB
                             00000032     01 - POP_TOP             
                             00000033     74 - LOAD_GLOBAL         'discovery'
                             00000036     69 - LOAD_ATTR           'serverPrint'
                             00000039     64 - LOAD_CONST          'SP: Crafting - Testing Recipe'
                             0000003C     83 - CALL_FUNCTION       r0001
                             0000003F     01 - POP_TOP             
                             00000040     7C - LOAD_FAST           'ingredients'
                             00000043     7C - LOAD_FAST           'recipe'
                             00000046     74 - LOAD_GLOBAL         'len'
                             00000049     7C - LOAD_FAST           'ingredients'
                             0000004C     83 - CALL_FUNCTION       r0001
                             0000004F     20 - SLICE+2             
                             00000050     6A - COMPARE_OP          "=="
                             00000053     6F - JUMP_IF_FALSE       -> 000000B7
                             00000056     01 - POP_TOP             
                             00000057     64 - LOAD_CONST          'SP: Crafting - Recipe '
                             0000005A     7D - STORE_FAST          'a_str'
                             0000005D     78 - SETUP_LOOP          -> 00000095
                             00000060     7C - LOAD_FAST           'recipe'
                             00000063     44 - GET_ITER            
                             00000064     5D - FOR_ITER            -> 00000094
                             00000067     7D - STORE_FAST          'item'
                             0000006A     74 - LOAD_GLOBAL         'discovery'
                             0000006D     69 - LOAD_ATTR           'getTypeInfo'
                             00000070     7C - LOAD_FAST           'item'
                             00000073     83 - CALL_FUNCTION       r0001
                             00000076     7D - STORE_FAST          'type_info'
                             00000079     7C - LOAD_FAST           'a_str'
                             0000007C     7C - LOAD_FAST           'type_info'
                             0000007F     64 - LOAD_CONST          'localname'
                             00000082     19 - BINARY_SUBSCR       
                             00000083     17 - BINARY_ADD          
                             00000084     7D - STORE_FAST          'a_str'
                             00000087     7C - LOAD_FAST           'a_str'
                             0000008A     64 - LOAD_CONST          '\n '
                             0000008D     17 - BINARY_ADD          
                             0000008E     7D - STORE_FAST          'a_str'
                             00000091     71 - JUMP_ABSOLUTE       -> 00000064
                             00000094     57 - POP_BLOCK           
                             00000095     74 - LOAD_GLOBAL         'discovery'
                             00000098     69 - LOAD_ATTR           'serverPrint'
                             0000009B     7C - LOAD_FAST           'a_str'
                             0000009E     83 - CALL_FUNCTION       r0001
                             000000A1     01 - POP_TOP             
                             000000A2     7C - LOAD_FAST           'recipe'
                             000000A5     74 - LOAD_GLOBAL         'len'
                             000000A8     7C - LOAD_FAST           'recipe'
                             000000AB     83 - CALL_FUNCTION       r0001
                             000000AE     64 - LOAD_CONST          1
                             000000B1     18 - BINARY_SUBTRACT     
                             000000B2     19 - BINARY_SUBSCR       
                             000000B3     53 - RETURN_VALUE        
                             000000B4     71 - JUMP_ABSOLUTE       -> 000000BC
                             000000B7     01 - POP_TOP             
                             000000B8     71 - JUMP_ABSOLUTE       -> 00000010
                             000000BB     01 - POP_TOP             
                             000000BC     71 - JUMP_ABSOLUTE       -> 00000010
                             000000BF     57 - POP_BLOCK           
                             000000C0     74 - LOAD_GLOBAL         'discovery'
                             000000C3     69 - LOAD_ATTR           'serverPrint'
                             000000C6     64 - LOAD_CONST          'SP: Crafting - No Matching Recipe Found'
                             000000C9     83 - CALL_FUNCTION       r0001
                             000000CC     01 - POP_TOP             
                             000000CD     64 - LOAD_CONST          0
                             000000D0     53 - RETURN_VALUE        
                             000000D1     64 - LOAD_CONST          None
                             000000D4     53 - RETURN_VALUE        
                         consts:
0000017F                     TUPLE: (
00000184                         STR: 'ingredients is a tuple of Game Obj IDs.  Return value is new Game Obj ID (zero for failure).' (5C 00 00 00 69 6E 67 72 65 64 69 65 6E 74 73 20 69 73 20 61 20 74 75 70 6C 65 20 6F 66 20 47 61 6D 65 20 4F 62 6A 20 49 44 73 2E 20 20 52 65 74 75 72 6E 20 76 61 6C 75 65 20 69 73 20 6E 65 77 20 47 61 6D 65 20 4F 62 6A 20 49 44 20 28 7A 65 72 6F 20 66 6F 72 20 66 61 69 6C 75 72 65 29 2E),
000001E5                         INT: 1 (01 00 00 00),
000001EA                         STR: 'SP: Crafting - Testing Recipe' (1D 00 00 00 53 50 3A 20 43 72 61 66 74 69 6E 67 20 2D 20 54 65 73 74 69 6E 67 20 52 65 63 69 70 65),
0000020C                         STR: 'SP: Crafting - Recipe ' (16 00 00 00 53 50 3A 20 43 72 61 66 74 69 6E 67 20 2D 20 52 65 63 69 70 65 20),
00000227                         STR: 'localname' (09 00 00 00 6C 6F 63 61 6C 6E 61 6D 65),
00000235                         STR: '\n ' (02 00 00 00 0A 20),
0000023C                         STR: 'SP: Crafting - No Matching Recipe Found' (27 00 00 00 53 50 3A 20 43 72 61 66 74 69 6E 67 20 2D 20 4E 6F 20 4D 61 74 63 68 69 6E 67 20 52 65 63 69 70 65 20 46 6F 75 6E 64),
00000268                         INT: 0 (00 00 00 00),
0000026D                         None (4E)
                             )
                         names:
0000026E                     TUPLE: (
00000273                         STR: 'globals' (07 00 00 00 67 6C 6F 62 61 6C 73),
0000027F                         STR: 'globs' (05 00 00 00 67 6C 6F 62 73),
00000289                         STR: 'Cookbook' (08 00 00 00 43 6F 6F 6B 62 6F 6F 6B),
00000296                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
000002A1                         STR: 'len' (03 00 00 00 6C 65 6E),
000002A9                         STR: 'ingredients' (0B 00 00 00 69 6E 67 72 65 64 69 65 6E 74 73),
000002B9                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000002C7                         STR: 'serverPrint' (0B 00 00 00 73 65 72 76 65 72 50 72 69 6E 74),
000002D7                         STR: 'a_str' (05 00 00 00 61 5F 73 74 72),
000002E1                         STR: 'item' (04 00 00 00 69 74 65 6D),
000002EA                         STR: 'getTypeInfo' (0B 00 00 00 67 65 74 54 79 70 65 49 6E 66 6F),
000002FA                         STR: 'type_info' (09 00 00 00 74 79 70 65 5F 69 6E 66 6F)
                             )
                         varnames:
00000308                     TUPLE: (
0000030D                         STR: 'ingredients' (0B 00 00 00 69 6E 67 72 65 64 69 65 6E 74 73),
0000031D                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
00000328                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000331                         STR: 'a_str' (05 00 00 00 61 5F 73 74 72),
0000033B                         STR: 'type_info' (09 00 00 00 74 79 70 65 5F 69 6E 66 6F),
00000349                         STR: 'globs' (05 00 00 00 67 6C 6F 62 73)
                             )
                         freevars:
00000353                     TUPLE: ()
                         cellvars:
00000358                     TUPLE: ()
                         filename:
0000035D                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\recipes.py' (3F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 72 65 63 69 70 65 73 2E 70 79)
                         name:
000003A1                     STR: 'CraftRecipe' (0B 00 00 00 43 72 61 66 74 52 65 63 69 70 65)
                         firslineno:
000003B1                     LONG: 32L (20 00 00 00)
                         lnotab:
000003B5                     STR: '\x00\x01\x00\x02\t\x02\x07\x00\x06\x03\x1d\x03\r\x01\x17\x02\x06\x01\x07\x00\x06\x01\x0f\x01\x0e\x01\x0e\x01\r\x02\x1e\x03\r\x01' (22 00 00 00 00 01 00 02 09 02 07 00 06 03 1D 03 0D 01 17 02 06 01 07 00 06 01 0F 01 0E 01 0E 01 0D 02 1E 03 0D 01),
000003DC             CODE:
                         argcount:
000003DD                     LONG: 1L (01 00 00 00)
                         nlocals:
000003E1                     LONG: 5L (05 00 00 00)
                         stacksize:
000003E5                     LONG: 4L (04 00 00 00)
                         flags:
000003E9                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000003ED                     STR: 'g\x00\x00}\x04\x00xm\x00t\x01\x00D]e\x00}\x01\x00|\x01\x00t\x03\x00|\x01\x00\x83\x01\x00d\x01\x00\x18\x19}\x02\x00t\x05\x00i\x06\x00|\x02\x00\x83\x01\x00}\x03\x00|\x03\x00o\r\x00\x01|\x03\x00i\x08\x00d\x02\x00\x83\x01\x00o%\x00\x01|\x00\x00|\x03\x00i\n\x00j\x00\x00o\x11\x00\x01|\x04\x00i\x0b\x00|\x02\x00\x83\x01\x00\x01qr\x00\x01q\r\x00\x01q\r\x00W|\x04\x00Sd\x03\x00S' (7E 00 00 00 67 00 00 7D 04 00 78 6D 00 74 01 00 44 5D 65 00 7D 01 00 7C 01 00 74 03 00 7C 01 00 83 01 00 64 01 00 18 19 7D 02 00 74 05 00 69 06 00 7C 02 00 83 01 00 7D 03 00 7C 03 00 6F 0D 00 01 7C 03 00 69 08 00 64 02 00 83 01 00 6F 25 00 01 7C 00 00 7C 03 00 69 0A 00 6A 00 00 6F 11 00 01 7C 04 00 69 0B 00 7C 02 00 83 01 00 01 71 72 00 01 71 0D 00 01 71 0D 00 57 7C 04 00 53 64 03 00 53)
                             00000000     67 - BUILD_LIST          r0000
                             00000003     7D - STORE_FAST          'obj_list'
                             00000006     78 - SETUP_LOOP          -> 00000076
                             00000009     74 - LOAD_GLOBAL         'Cookbook'
                             0000000C     44 - GET_ITER            
                             0000000D     5D - FOR_ITER            -> 00000075
                             00000010     7D - STORE_FAST          'recipe'
                             00000013     7C - LOAD_FAST           'recipe'
                             00000016     74 - LOAD_GLOBAL         'len'
                             00000019     7C - LOAD_FAST           'recipe'
                             0000001C     83 - CALL_FUNCTION       r0001
                             0000001F     64 - LOAD_CONST          1
                             00000022     18 - BINARY_SUBTRACT     
                             00000023     19 - BINARY_SUBSCR       
                             00000024     7D - STORE_FAST          'item'
                             00000027     74 - LOAD_GLOBAL         'discovery'
                             0000002A     69 - LOAD_ATTR           'getTypeInfo'
                             0000002D     7C - LOAD_FAST           'item'
                             00000030     83 - CALL_FUNCTION       r0001
                             00000033     7D - STORE_FAST          'type_info'
                             00000036     7C - LOAD_FAST           'type_info'
                             00000039     6F - JUMP_IF_FALSE       -> 00000049
                             0000003C     01 - POP_TOP             
                             0000003D     7C - LOAD_FAST           'type_info'
                             00000040     69 - LOAD_ATTR           'has_key'
                             00000043     64 - LOAD_CONST          'Complexity'
                             00000046     83 - CALL_FUNCTION       r0001
                             00000049     6F - JUMP_IF_FALSE       -> 00000071
                             0000004C     01 - POP_TOP             
                             0000004D     7C - LOAD_FAST           'level'
                             00000050     7C - LOAD_FAST           'type_info'
                             00000053     69 - LOAD_ATTR           'Complexity'
                             00000056     6A - COMPARE_OP          "<"
                             00000059     6F - JUMP_IF_FALSE       -> 0000006D
                             0000005C     01 - POP_TOP             
                             0000005D     7C - LOAD_FAST           'obj_list'
                             00000060     69 - LOAD_ATTR           'append'
                             00000063     7C - LOAD_FAST           'item'
                             00000066     83 - CALL_FUNCTION       r0001
                             00000069     01 - POP_TOP             
                             0000006A     71 - JUMP_ABSOLUTE       -> 00000072
                             0000006D     01 - POP_TOP             
                             0000006E     71 - JUMP_ABSOLUTE       -> 0000000D
                             00000071     01 - POP_TOP             
                             00000072     71 - JUMP_ABSOLUTE       -> 0000000D
                             00000075     57 - POP_BLOCK           
                             00000076     7C - LOAD_FAST           'obj_list'
                             00000079     53 - RETURN_VALUE        
                             0000007A     64 - LOAD_CONST          None
                             0000007D     53 - RETURN_VALUE        
                         consts:
00000470                     TUPLE: (
00000475                         STR: ' find the recipes for level ' (1C 00 00 00 20 66 69 6E 64 20 74 68 65 20 72 65 63 69 70 65 73 20 66 6F 72 20 6C 65 76 65 6C 20),
00000496                         INT: 1 (01 00 00 00),
0000049B                         STR: 'Complexity' (0A 00 00 00 43 6F 6D 70 6C 65 78 69 74 79),
000004AA                         None (4E)
                             )
                         names:
000004AB                     TUPLE: (
000004B0                         STR: 'obj_list' (08 00 00 00 6F 62 6A 5F 6C 69 73 74),
000004BD                         STR: 'Cookbook' (08 00 00 00 43 6F 6F 6B 62 6F 6F 6B),
000004CA                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
000004D5                         STR: 'len' (03 00 00 00 6C 65 6E),
000004DD                         STR: 'item' (04 00 00 00 69 74 65 6D),
000004E6                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000004F4                         STR: 'getTypeInfo' (0B 00 00 00 67 65 74 54 79 70 65 49 6E 66 6F),
00000504                         STR: 'type_info' (09 00 00 00 74 79 70 65 5F 69 6E 66 6F),
00000512                         STR: 'has_key' (07 00 00 00 68 61 73 5F 6B 65 79),
0000051E                         STR: 'level' (05 00 00 00 6C 65 76 65 6C),
00000528                         STR: 'Complexity' (0A 00 00 00 43 6F 6D 70 6C 65 78 69 74 79),
00000537                         STR: 'append' (06 00 00 00 61 70 70 65 6E 64)
                             )
                         varnames:
00000542                     TUPLE: (
00000547                         STR: 'level' (05 00 00 00 6C 65 76 65 6C),
00000551                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
0000055C                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000565                         STR: 'type_info' (09 00 00 00 74 79 70 65 5F 69 6E 66 6F),
00000573                         STR: 'obj_list' (08 00 00 00 6F 62 6A 5F 6C 69 73 74)
                             )
                         freevars:
00000580                     TUPLE: ()
                         cellvars:
00000585                     TUPLE: ()
                         filename:
0000058A                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\recipes.py' (3F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 72 65 63 69 70 65 73 2E 70 79)
                         name:
000005CE                     STR: 'GetRecipesForWriteCodeLevel' (1B 00 00 00 47 65 74 52 65 63 69 70 65 73 46 6F 72 57 72 69 74 65 43 6F 64 65 4C 65 76 65 6C)
                         firslineno:
000005EE                     LONG: 62L (3E 00 00 00)
                         lnotab:
000005F2                     STR: '\x00\x01\x00\x02\x06\x01\x07\x00\x06\x01\x14\x01\x0f\x01\x17\x01\x10\x01\x19\x03' (14 00 00 00 00 01 00 02 06 01 07 00 06 01 14 01 0F 01 17 01 10 01 19 03),
0000060B             CODE:
                         argcount:
0000060C                     LONG: 1L (01 00 00 00)
                         nlocals:
00000610                     LONG: 3L (03 00 00 00)
                         stacksize:
00000614                     LONG: 6L (06 00 00 00)
                         flags:
00000618                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000061C                     STR: 'd\x01\x00G|\x00\x00GHx\x81\x00t\x01\x00D]y\x00}\x02\x00|\x00\x00|\x02\x00t\x03\x00|\x02\x00\x83\x01\x00d\x02\x00\x18\x19j\x02\x00oX\x00\x01|\x02\x00d\x03\x00t\x03\x00|\x02\x00\x83\x01\x00d\x02\x00\x18!}\x01\x00d\x04\x00G|\x02\x00d\x03\x00t\x03\x00|\x02\x00\x83\x01\x00d\x02\x00\x18!Gd\x05\x00Gt\x05\x00|\x02\x00d\x03\x00t\x03\x00|\x02\x00\x83\x01\x00d\x02\x00\x18!\x83\x01\x00GH|\x01\x00Sq\x10\x00\x01q\x10\x00Wt\x06\x00Sd\x06\x00S' (95 00 00 00 64 01 00 47 7C 00 00 47 48 78 81 00 74 01 00 44 5D 79 00 7D 02 00 7C 00 00 7C 02 00 74 03 00 7C 02 00 83 01 00 64 02 00 18 19 6A 02 00 6F 58 00 01 7C 02 00 64 03 00 74 03 00 7C 02 00 83 01 00 64 02 00 18 21 7D 01 00 64 04 00 47 7C 02 00 64 03 00 74 03 00 7C 02 00 83 01 00 64 02 00 18 21 47 64 05 00 47 74 05 00 7C 02 00 64 03 00 74 03 00 7C 02 00 83 01 00 64 02 00 18 21 83 01 00 47 48 7C 01 00 53 71 10 00 01 71 10 00 57 74 06 00 53 64 06 00 53)
                             00000000     64 - LOAD_CONST          'getting recipe for '
                             00000003     47 - PRINT_ITEM          
                             00000004     7C - LOAD_FAST           'obj'
                             00000007     47 - PRINT_ITEM          
                             00000008     48 - PRINT_NEWLINE       
                             00000009     78 - SETUP_LOOP          -> 0000008D
                             0000000C     74 - LOAD_GLOBAL         'Cookbook'
                             0000000F     44 - GET_ITER            
                             00000010     5D - FOR_ITER            -> 0000008C
                             00000013     7D - STORE_FAST          'recipe'
                             00000016     7C - LOAD_FAST           'obj'
                             00000019     7C - LOAD_FAST           'recipe'
                             0000001C     74 - LOAD_GLOBAL         'len'
                             0000001F     7C - LOAD_FAST           'recipe'
                             00000022     83 - CALL_FUNCTION       r0001
                             00000025     64 - LOAD_CONST          1
                             00000028     18 - BINARY_SUBTRACT     
                             00000029     19 - BINARY_SUBSCR       
                             0000002A     6A - COMPARE_OP          "=="
                             0000002D     6F - JUMP_IF_FALSE       -> 00000088
                             00000030     01 - POP_TOP             
                             00000031     7C - LOAD_FAST           'recipe'
                             00000034     64 - LOAD_CONST          0
                             00000037     74 - LOAD_GLOBAL         'len'
                             0000003A     7C - LOAD_FAST           'recipe'
                             0000003D     83 - CALL_FUNCTION       r0001
                             00000040     64 - LOAD_CONST          1
                             00000043     18 - BINARY_SUBTRACT     
                             00000044     21 - SLICE+3             
                             00000045     7D - STORE_FAST          'foo'
                             00000048     64 - LOAD_CONST          'Get recipe : '
                             0000004B     47 - PRINT_ITEM          
                             0000004C     7C - LOAD_FAST           'recipe'
                             0000004F     64 - LOAD_CONST          0
                             00000052     74 - LOAD_GLOBAL         'len'
                             00000055     7C - LOAD_FAST           'recipe'
                             00000058     83 - CALL_FUNCTION       r0001
                             0000005B     64 - LOAD_CONST          1
                             0000005E     18 - BINARY_SUBTRACT     
                             0000005F     21 - SLICE+3             
                             00000060     47 - PRINT_ITEM          
                             00000061     64 - LOAD_CONST          ' type : '
                             00000064     47 - PRINT_ITEM          
                             00000065     74 - LOAD_GLOBAL         'type'
                             00000068     7C - LOAD_FAST           'recipe'
                             0000006B     64 - LOAD_CONST          0
                             0000006E     74 - LOAD_GLOBAL         'len'
                             00000071     7C - LOAD_FAST           'recipe'
                             00000074     83 - CALL_FUNCTION       r0001
                             00000077     64 - LOAD_CONST          1
                             0000007A     18 - BINARY_SUBTRACT     
                             0000007B     21 - SLICE+3             
                             0000007C     83 - CALL_FUNCTION       r0001
                             0000007F     47 - PRINT_ITEM          
                             00000080     48 - PRINT_NEWLINE       
                             00000081     7C - LOAD_FAST           'foo'
                             00000084     53 - RETURN_VALUE        
                             00000085     71 - JUMP_ABSOLUTE       -> 00000010
                             00000088     01 - POP_TOP             
                             00000089     71 - JUMP_ABSOLUTE       -> 00000010
                             0000008C     57 - POP_BLOCK           
                             0000008D     74 - LOAD_GLOBAL         'None'
                             00000090     53 - RETURN_VALUE        
                             00000091     64 - LOAD_CONST          None
                             00000094     53 - RETURN_VALUE        
                         consts:
000006B6                     TUPLE: (
000006BB                         STR: ' find the recipe for the object ' (20 00 00 00 20 66 69 6E 64 20 74 68 65 20 72 65 63 69 70 65 20 66 6F 72 20 74 68 65 20 6F 62 6A 65 63 74 20),
000006E0                         STR: 'getting recipe for ' (13 00 00 00 67 65 74 74 69 6E 67 20 72 65 63 69 70 65 20 66 6F 72 20),
000006F8                         INT: 1 (01 00 00 00),
000006FD                         INT: 0 (00 00 00 00),
00000702                         STR: 'Get recipe : ' (0D 00 00 00 47 65 74 20 72 65 63 69 70 65 20 3A 20),
00000714                         STR: ' type : ' (08 00 00 00 20 74 79 70 65 20 3A 20),
00000721                         None (4E)
                             )
                         names:
00000722                     TUPLE: (
00000727                         STR: 'obj' (03 00 00 00 6F 62 6A),
0000072F                         STR: 'Cookbook' (08 00 00 00 43 6F 6F 6B 62 6F 6F 6B),
0000073C                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
00000747                         STR: 'len' (03 00 00 00 6C 65 6E),
0000074F                         STR: 'foo' (03 00 00 00 66 6F 6F),
00000757                         STR: 'type' (04 00 00 00 74 79 70 65),
00000760                         STR: 'None' (04 00 00 00 4E 6F 6E 65)
                             )
                         varnames:
00000769                     TUPLE: (
0000076E                         STR: 'obj' (03 00 00 00 6F 62 6A),
00000776                         STR: 'foo' (03 00 00 00 66 6F 6F),
0000077E                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65)
                             )
                         freevars:
00000789                     TUPLE: ()
                         cellvars:
0000078E                     TUPLE: ()
                         filename:
00000793                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\recipes.py' (3F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 72 65 63 69 70 65 73 2E 70 79)
                         name:
000007D7                     STR: 'GetRecipesForObject' (13 00 00 00 47 65 74 52 65 63 69 70 65 73 46 6F 72 4F 62 6A 65 63 74)
                         firslineno:
000007EF                     LONG: 79L (4F 00 00 00)
                         lnotab:
000007F3                     STR: '\x00\x01\x00\x01\t\x02\x07\x00\x06\x01\x1b\x02\x17\x019\x01\x0c\x02' (12 00 00 00 00 01 00 01 09 02 07 00 06 01 1B 02 17 01 39 01 0C 02),
0000080A             CODE:
                         argcount:
0000080B                     LONG: 0L (00 00 00 00)
                         nlocals:
0000080F                     LONG: 0L (00 00 00 00)
                         stacksize:
00000813                     LONG: 2L (02 00 00 00)
                         flags:
00000817                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
0000081B                     STR: 't\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x01\x00d\x02\x00\x83\x01\x00\x01t\x00\x00i\x01\x00d\x01\x00\x83\x01\x00\x01t\x00\x00i\x02\x00d\x03\x00\x83\x01\x00\x01d\x00\x00S' (38 00 00 00 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 01 00 64 02 00 83 01 00 01 74 00 00 69 01 00 64 01 00 83 01 00 01 74 00 00 69 02 00 64 03 00 83 01 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'discovery'
                             00000003     69 - LOAD_ATTR           'outputDebugString'
                             00000006     64 - LOAD_CONST          '-------------------------------------------------\n'
                             00000009     83 - CALL_FUNCTION       r0001
                             0000000C     01 - POP_TOP             
                             0000000D     74 - LOAD_GLOBAL         'discovery'
                             00000010     69 - LOAD_ATTR           'outputDebugString'
                             00000013     64 - LOAD_CONST          'python- code fragment recipes loaded.\n'
                             00000016     83 - CALL_FUNCTION       r0001
                             00000019     01 - POP_TOP             
                             0000001A     74 - LOAD_GLOBAL         'discovery'
                             0000001D     69 - LOAD_ATTR           'outputDebugString'
                             00000020     64 - LOAD_CONST          '-------------------------------------------------\n'
                             00000023     83 - CALL_FUNCTION       r0001
                             00000026     01 - POP_TOP             
                             00000027     74 - LOAD_GLOBAL         'discovery'
                             0000002A     69 - LOAD_ATTR           'serverPrint'
                             0000002D     64 - LOAD_CONST          'SP: Code Fragment Recipes Functioning'
                             00000030     83 - CALL_FUNCTION       r0001
                             00000033     01 - POP_TOP             
                             00000034     64 - LOAD_CONST          None
                             00000037     53 - RETURN_VALUE        
                         consts:
00000858                     TUPLE: (
0000085D                         None (4E),
0000085E                         STR: '-------------------------------------------------\n' (32 00 00 00 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0A),
00000895                         STR: 'python- code fragment recipes loaded.\n' (26 00 00 00 70 79 74 68 6F 6E 2D 20 63 6F 64 65 20 66 72 61 67 6D 65 6E 74 20 72 65 63 69 70 65 73 20 6C 6F 61 64 65 64 2E 0A),
000008C0                         STR: 'SP: Code Fragment Recipes Functioning' (25 00 00 00 53 50 3A 20 43 6F 64 65 20 46 72 61 67 6D 65 6E 74 20 52 65 63 69 70 65 73 20 46 75 6E 63 74 69 6F 6E 69 6E 67)
                             )
                         names:
000008EA                     TUPLE: (
000008EF                         STR: 'discovery' (09 00 00 00 64 69 73 63 6F 76 65 72 79),
000008FD                         STR: 'outputDebugString' (11 00 00 00 6F 75 74 70 75 74 44 65 62 75 67 53 74 72 69 6E 67),
00000913                         STR: 'serverPrint' (0B 00 00 00 73 65 72 76 65 72 50 72 69 6E 74)
                             )
                         varnames:
00000923                     TUPLE: ()
                         freevars:
00000928                     TUPLE: ()
                         cellvars:
0000092D                     TUPLE: ()
                         filename:
00000932                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\recipes.py' (3F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 72 65 63 69 70 65 73 2E 70 79)
                         name:
00000976                     STR: 'debugTest' (09 00 00 00 64 65 62 75 67 54 65 73 74)
                         firslineno:
00000984                     LONG: 103L (67 00 00 00)
                         lnotab:
00000988                     STR: '\x00\x01\r\x01\r\x01\r\x01' (08 00 00 00 00 01 0D 01 0D 01 0D 01),
00000995             CODE:
                         argcount:
00000996                     LONG: 0L (00 00 00 00)
                         nlocals:
0000099A                     LONG: 4L (04 00 00 00)
                         stacksize:
0000099E                     LONG: 6L (06 00 00 00)
                         flags:
000009A2                     LONG: 67L (43 00 00 00)
                             (OPTIMIZED, NEWLOCALS, NOFREE)
                         code:
000009A6                     STR: 't\x00\x00d\x01\x00d\x02\x00\x83\x02\x00}\x03\x00xy\x00t\x02\x00D]q\x00}\x01\x00|\x01\x00t\x04\x00|\x01\x00\x83\x01\x00d\x03\x00\x18\x19}\x02\x00|\x03\x00i\x06\x00d\x04\x00|\x02\x00\x16\x83\x01\x00\x01x6\x00t\x07\x00d\x05\x00t\x04\x00|\x01\x00\x83\x01\x00d\x03\x00\x18\x83\x02\x00D]\x1b\x00}\x00\x00|\x03\x00i\x06\x00d\x04\x00|\x01\x00|\x00\x00\x19\x16\x83\x01\x00\x01q[\x00W|\x03\x00i\x06\x00d\x06\x00\x83\x01\x00\x01q\x16\x00W|\x03\x00i\t\x00\x83\x00\x00\x01d\x00\x00S' (99 00 00 00 74 00 00 64 01 00 64 02 00 83 02 00 7D 03 00 78 79 00 74 02 00 44 5D 71 00 7D 01 00 7C 01 00 74 04 00 7C 01 00 83 01 00 64 03 00 18 19 7D 02 00 7C 03 00 69 06 00 64 04 00 7C 02 00 16 83 01 00 01 78 36 00 74 07 00 64 05 00 74 04 00 7C 01 00 83 01 00 64 03 00 18 83 02 00 44 5D 1B 00 7D 00 00 7C 03 00 69 06 00 64 04 00 7C 01 00 7C 00 00 19 16 83 01 00 01 71 5B 00 57 7C 03 00 69 06 00 64 06 00 83 01 00 01 71 16 00 57 7C 03 00 69 09 00 83 00 00 01 64 00 00 53)
                             00000000     74 - LOAD_GLOBAL         'open'
                             00000003     64 - LOAD_CONST          'c:/matrix/game/matrix/resource/Python/Monolith/clientcookbook.txt'
                             00000006     64 - LOAD_CONST          'w'
                             00000009     83 - CALL_FUNCTION       r0002
                             0000000C     7D - STORE_FAST          'file'
                             0000000F     78 - SETUP_LOOP          -> 0000008B
                             00000012     74 - LOAD_GLOBAL         'Cookbook'
                             00000015     44 - GET_ITER            
                             00000016     5D - FOR_ITER            -> 0000008A
                             00000019     7D - STORE_FAST          'recipe'
                             0000001C     7C - LOAD_FAST           'recipe'
                             0000001F     74 - LOAD_GLOBAL         'len'
                             00000022     7C - LOAD_FAST           'recipe'
                             00000025     83 - CALL_FUNCTION       r0001
                             00000028     64 - LOAD_CONST          1
                             0000002B     18 - BINARY_SUBTRACT     
                             0000002C     19 - BINARY_SUBSCR       
                             0000002D     7D - STORE_FAST          'item'
                             00000030     7C - LOAD_FAST           'file'
                             00000033     69 - LOAD_ATTR           'write'
                             00000036     64 - LOAD_CONST          '%i '
                             00000039     7C - LOAD_FAST           'item'
                             0000003C     16 - BINARY_MODULO       
                             0000003D     83 - CALL_FUNCTION       r0001
                             00000040     01 - POP_TOP             
                             00000041     78 - SETUP_LOOP          -> 0000007A
                             00000044     74 - LOAD_GLOBAL         'range'
                             00000047     64 - LOAD_CONST          0
                             0000004A     74 - LOAD_GLOBAL         'len'
                             0000004D     7C - LOAD_FAST           'recipe'
                             00000050     83 - CALL_FUNCTION       r0001
                             00000053     64 - LOAD_CONST          1
                             00000056     18 - BINARY_SUBTRACT     
                             00000057     83 - CALL_FUNCTION       r0002
                             0000005A     44 - GET_ITER            
                             0000005B     5D - FOR_ITER            -> 00000079
                             0000005E     7D - STORE_FAST          'i'
                             00000061     7C - LOAD_FAST           'file'
                             00000064     69 - LOAD_ATTR           'write'
                             00000067     64 - LOAD_CONST          '%i '
                             0000006A     7C - LOAD_FAST           'recipe'
                             0000006D     7C - LOAD_FAST           'i'
                             00000070     19 - BINARY_SUBSCR       
                             00000071     16 - BINARY_MODULO       
                             00000072     83 - CALL_FUNCTION       r0001
                             00000075     01 - POP_TOP             
                             00000076     71 - JUMP_ABSOLUTE       -> 0000005B
                             00000079     57 - POP_BLOCK           
                             0000007A     7C - LOAD_FAST           'file'
                             0000007D     69 - LOAD_ATTR           'write'
                             00000080     64 - LOAD_CONST          '\n'
                             00000083     83 - CALL_FUNCTION       r0001
                             00000086     01 - POP_TOP             
                             00000087     71 - JUMP_ABSOLUTE       -> 00000016
                             0000008A     57 - POP_BLOCK           
                             0000008B     7C - LOAD_FAST           'file'
                             0000008E     69 - LOAD_ATTR           'close'
                             00000091     83 - CALL_FUNCTION       r0000
                             00000094     01 - POP_TOP             
                             00000095     64 - LOAD_CONST          None
                             00000098     53 - RETURN_VALUE        
                         consts:
00000A44                     TUPLE: (
00000A49                         None (4E),
00000A4A                         STR: 'c:/matrix/game/matrix/resource/Python/Monolith/clientcookbook.txt' (41 00 00 00 63 3A 2F 6D 61 74 72 69 78 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 2F 50 79 74 68 6F 6E 2F 4D 6F 6E 6F 6C 69 74 68 2F 63 6C 69 65 6E 74 63 6F 6F 6B 62 6F 6F 6B 2E 74 78 74),
00000A90                         STR: 'w' (01 00 00 00 77),
00000A96                         INT: 1 (01 00 00 00),
00000A9B                         STR: '%i ' (03 00 00 00 25 69 20),
00000AA3                         INT: 0 (00 00 00 00),
00000AA8                         STR: '\n' (01 00 00 00 0A)
                             )
                         names:
00000AAE                     TUPLE: (
00000AB3                         STR: 'open' (04 00 00 00 6F 70 65 6E),
00000ABC                         STR: 'file' (04 00 00 00 66 69 6C 65),
00000AC5                         STR: 'Cookbook' (08 00 00 00 43 6F 6F 6B 62 6F 6F 6B),
00000AD2                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
00000ADD                         STR: 'len' (03 00 00 00 6C 65 6E),
00000AE5                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000AEE                         STR: 'write' (05 00 00 00 77 72 69 74 65),
00000AF8                         STR: 'range' (05 00 00 00 72 61 6E 67 65),
00000B02                         STR: 'i' (01 00 00 00 69),
00000B08                         STR: 'close' (05 00 00 00 63 6C 6F 73 65)
                             )
                         varnames:
00000B12                     TUPLE: (
00000B17                         STR: 'i' (01 00 00 00 69),
00000B1D                         STR: 'recipe' (06 00 00 00 72 65 63 69 70 65),
00000B28                         STR: 'item' (04 00 00 00 69 74 65 6D),
00000B31                         STR: 'file' (04 00 00 00 66 69 6C 65)
                             )
                         freevars:
00000B3A                     TUPLE: ()
                         cellvars:
00000B3F                     TUPLE: ()
                         filename:
00000B44                     STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\recipes.py' (3F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 72 65 63 69 70 65 73 2E 70 79)
                         name:
00000B88                     STR: 'WriteOutCookbook' (10 00 00 00 57 72 69 74 65 4F 75 74 43 6F 6F 6B 62 6F 6F 6B)
                         firslineno:
00000B9D                     LONG: 111L (6F 00 00 00)
                         lnotab:
00000BA1                     STR: '\x00\x01\x0f\x02\x07\x00\x06\x02\x14\x01\x11\x02\x1a\x00\x06\x01\x19\x02\x11\x02' (14 00 00 00 00 01 0F 02 07 00 06 02 14 01 11 02 1A 00 06 01 19 02 11 02)
                 )
             names:
00000BBA         TUPLE: (
00000BBF             STR: 'obj' (03 00 00 00 6F 62 6A),
00000BC7             STR: 'CodeFragmentB' (0D 00 00 00 43 6F 64 65 46 72 61 67 6D 65 6E 74 42),
00000BD9             STR: 'CodeFragmentC' (0D 00 00 00 43 6F 64 65 46 72 61 67 6D 65 6E 74 43),
00000BEB             STR: 'TapDataNodeAbility' (12 00 00 00 54 61 70 44 61 74 61 4E 6F 64 65 41 62 69 6C 69 74 79),
00000C02             STR: 'AnalyzeWeaknessTool' (13 00 00 00 41 6E 61 6C 79 7A 65 57 65 61 6B 6E 65 73 73 54 6F 6F 6C),
00000C1A             STR: 'Cookbook' (08 00 00 00 43 6F 6F 6B 62 6F 6F 6B),
00000C27             STR: 'CraftRecipe' (0B 00 00 00 43 72 61 66 74 52 65 63 69 70 65),
00000C37             STR: 'GetRecipesForWriteCodeLevel' (1B 00 00 00 47 65 74 52 65 63 69 70 65 73 46 6F 72 57 72 69 74 65 43 6F 64 65 4C 65 76 65 6C),
00000C57             STR: 'GetRecipesForObject' (13 00 00 00 47 65 74 52 65 63 69 70 65 73 46 6F 72 4F 62 6A 65 63 74),
00000C6F             STR: 'debugTest' (09 00 00 00 64 65 62 75 67 54 65 73 74),
00000C7D             STR: 'WriteOutCookbook' (10 00 00 00 57 72 69 74 65 4F 75 74 43 6F 6F 6B 62 6F 6F 6B)
                 )
             varnames:
00000C92         TUPLE: (
00000C97             STR: 'Cookbook' (08 00 00 00 43 6F 6F 6B 62 6F 6F 6B),
00000CA4             STR: 'obj' (03 00 00 00 6F 62 6A),
00000CAC             STR: 'WriteOutCookbook' (10 00 00 00 57 72 69 74 65 4F 75 74 43 6F 6F 6B 62 6F 6F 6B),
00000CC1             STR: 'GetRecipesForWriteCodeLevel' (1B 00 00 00 47 65 74 52 65 63 69 70 65 73 46 6F 72 57 72 69 74 65 43 6F 64 65 4C 65 76 65 6C),
00000CE1             STR: 'GetRecipesForObject' (13 00 00 00 47 65 74 52 65 63 69 70 65 73 46 6F 72 4F 62 6A 65 63 74),
00000CF9             STR: 'debugTest' (09 00 00 00 64 65 62 75 67 54 65 73 74),
00000D07             STR: 'CraftRecipe' (0B 00 00 00 43 72 61 66 74 52 65 63 69 70 65)
                 )
             freevars:
00000D17         TUPLE: ()
             cellvars:
00000D1C         TUPLE: ()
             filename:
00000D21         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\recipes.py' (3F 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 72 65 63 69 70 65 73 2E 70 79)
             name:
00000D65         STR: '?' (01 00 00 00 3F)
             firslineno:
00000D6B         LONG: 10L (0A 00 00 00)
             lnotab:
00000D6F         STR: '\t\x0b6\x0b\t\x1e\t\x11\t\x18\t\x08' (0C 00 00 00 09 0B 36 0B 09 1E 09 11 09 18 09 08)

