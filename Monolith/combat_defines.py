--== Disasm ==--
00000008 CODE:
             argcount:
00000009         LONG: 0L (00 00 00 00)
             nlocals:
0000000D         LONG: 0L (00 00 00 00)
             stacksize:
00000011         LONG: 2L (02 00 00 00)
             flags:
00000015         LONG: 64L (40 00 00 00)
                 (NOFREE)
             code:
00000019         STR: 'e\x00\x00i\x01\x00i\x02\x00e\x00\x00i\x01\x00i\x03\x00Be\x00\x00i\x01\x00i\x04\x00Be\x00\x00i\x01\x00i\x05\x00Be\x00\x00i\x01\x00i\x06\x00Be\x00\x00i\x01\x00i\x07\x00BZ\x08\x00d\x00\x00e\x08\x00\x0f@Z\t\x00e\x00\x00i\x01\x00i\x04\x00e\x00\x00i\x01\x00i\x05\x00Be\x00\x00i\x01\x00i\x06\x00Be\x00\x00i\x01\x00i\x07\x00BZ\n\x00d\x01\x00S' (77 00 00 00 65 00 00 69 01 00 69 02 00 65 00 00 69 01 00 69 03 00 42 65 00 00 69 01 00 69 04 00 42 65 00 00 69 01 00 69 05 00 42 65 00 00 69 01 00 69 06 00 42 65 00 00 69 01 00 69 07 00 42 5A 08 00 64 00 00 65 08 00 0F 40 5A 09 00 65 00 00 69 01 00 69 04 00 65 00 00 69 01 00 69 05 00 42 65 00 00 69 01 00 69 06 00 42 65 00 00 69 01 00 69 07 00 42 5A 0A 00 64 01 00 53)
                 00000000     65 - LOAD_NAME           'constants'
                 00000003     69 - LOAD_ATTR           'combat_prone'
                 00000006     69 - LOAD_ATTR           'LAYING_FACEDOWN'
                 00000009     65 - LOAD_NAME           'constants'
                 0000000C     69 - LOAD_ATTR           'combat_prone'
                 0000000F     69 - LOAD_ATTR           'LAYING_FACEUP'
                 00000012     42 - BINARY_OR           
                 00000013     65 - LOAD_NAME           'constants'
                 00000016     69 - LOAD_ATTR           'combat_prone'
                 00000019     69 - LOAD_ATTR           'VISUAL_FACEDOWN'
                 0000001C     42 - BINARY_OR           
                 0000001D     65 - LOAD_NAME           'constants'
                 00000020     69 - LOAD_ATTR           'combat_prone'
                 00000023     69 - LOAD_ATTR           'VISUAL_FACEUP'
                 00000026     42 - BINARY_OR           
                 00000027     65 - LOAD_NAME           'constants'
                 0000002A     69 - LOAD_ATTR           'combat_prone'
                 0000002D     69 - LOAD_ATTR           'I_LB_TRANSITION'
                 00000030     42 - BINARY_OR           
                 00000031     65 - LOAD_NAME           'constants'
                 00000034     69 - LOAD_ATTR           'combat_prone'
                 00000037     69 - LOAD_ATTR           'V_LB_TRANSITION'
                 0000003A     42 - BINARY_OR           
                 0000003B     5A - STORE_NAME          'COMBAT_CONTROLLED_MASK'
                 0000003E     64 - LOAD_CONST          -1
                 00000041     65 - LOAD_NAME           'COMBAT_CONTROLLED_MASK'
                 00000044     0F - UNARY_INVERT        
                 00000045     40 - BINARY_AND          
                 00000046     5A - STORE_NAME          'ABILITY_CONTROLLED_MASK'
                 00000049     65 - LOAD_NAME           'constants'
                 0000004C     69 - LOAD_ATTR           'combat_prone'
                 0000004F     69 - LOAD_ATTR           'VISUAL_FACEDOWN'
                 00000052     65 - LOAD_NAME           'constants'
                 00000055     69 - LOAD_ATTR           'combat_prone'
                 00000058     69 - LOAD_ATTR           'VISUAL_FACEUP'
                 0000005B     42 - BINARY_OR           
                 0000005C     65 - LOAD_NAME           'constants'
                 0000005F     69 - LOAD_ATTR           'combat_prone'
                 00000062     69 - LOAD_ATTR           'I_LB_TRANSITION'
                 00000065     42 - BINARY_OR           
                 00000066     65 - LOAD_NAME           'constants'
                 00000069     69 - LOAD_ATTR           'combat_prone'
                 0000006C     69 - LOAD_ATTR           'V_LB_TRANSITION'
                 0000006F     42 - BINARY_OR           
                 00000070     5A - STORE_NAME          'PRONE_RECOVERY_INSTANT'
                 00000073     64 - LOAD_CONST          None
                 00000076     53 - RETURN_VALUE        
             consts:
00000095         TUPLE: (
0000009A             INT: -1 (FF FF FF FF),
0000009F             None (4E)
                 )
             names:
000000A0         TUPLE: (
000000A5             STR: 'constants' (09 00 00 00 63 6F 6E 73 74 61 6E 74 73),
000000B3             STR: 'combat_prone' (0C 00 00 00 63 6F 6D 62 61 74 5F 70 72 6F 6E 65),
000000C4             STR: 'LAYING_FACEDOWN' (0F 00 00 00 4C 41 59 49 4E 47 5F 46 41 43 45 44 4F 57 4E),
000000D8             STR: 'LAYING_FACEUP' (0D 00 00 00 4C 41 59 49 4E 47 5F 46 41 43 45 55 50),
000000EA             STR: 'VISUAL_FACEDOWN' (0F 00 00 00 56 49 53 55 41 4C 5F 46 41 43 45 44 4F 57 4E),
000000FE             STR: 'VISUAL_FACEUP' (0D 00 00 00 56 49 53 55 41 4C 5F 46 41 43 45 55 50),
00000110             STR: 'I_LB_TRANSITION' (0F 00 00 00 49 5F 4C 42 5F 54 52 41 4E 53 49 54 49 4F 4E),
00000124             STR: 'V_LB_TRANSITION' (0F 00 00 00 56 5F 4C 42 5F 54 52 41 4E 53 49 54 49 4F 4E),
00000138             STR: 'COMBAT_CONTROLLED_MASK' (16 00 00 00 43 4F 4D 42 41 54 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 4D 41 53 4B),
00000153             STR: 'ABILITY_CONTROLLED_MASK' (17 00 00 00 41 42 49 4C 49 54 59 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 4D 41 53 4B),
0000016F             STR: 'PRONE_RECOVERY_INSTANT' (16 00 00 00 50 52 4F 4E 45 5F 52 45 43 4F 56 45 52 59 5F 49 4E 53 54 41 4E 54)
                 )
             varnames:
0000018A         TUPLE: (
0000018F             STR: 'PRONE_RECOVERY_INSTANT' (16 00 00 00 50 52 4F 4E 45 5F 52 45 43 4F 56 45 52 59 5F 49 4E 53 54 41 4E 54),
000001AA             STR: 'ABILITY_CONTROLLED_MASK' (17 00 00 00 41 42 49 4C 49 54 59 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 4D 41 53 4B),
000001C6             STR: 'COMBAT_CONTROLLED_MASK' (16 00 00 00 43 4F 4D 42 41 54 5F 43 4F 4E 54 52 4F 4C 4C 45 44 5F 4D 41 53 4B)
                 )
             freevars:
000001E1         TUPLE: ()
             cellvars:
000001E6         TUPLE: ()
             filename:
000001EB         STR: 'c:/PatchStaging/game/matrix/resource\\Python\\Monolith\\combat_defines.py' (46 00 00 00 63 3A 2F 50 61 74 63 68 53 74 61 67 69 6E 67 2F 67 61 6D 65 2F 6D 61 74 72 69 78 2F 72 65 73 6F 75 72 63 65 5C 50 79 74 68 6F 6E 5C 4D 6F 6E 6F 6C 69 74 68 5C 63 6F 6D 62 61 74 5F 64 65 66 69 6E 65 73 2E 70 79)
             name:
00000236         STR: '?' (01 00 00 00 3F)
             firslineno:
0000023C         LONG: 1L (01 00 00 00)
             lnotab:
00000240         STR: '>\x01\x0b\x01' (04 00 00 00 3E 01 0B 01)

