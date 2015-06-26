# File: s (Python 2.4)

from pandac.PandaModules import Point3, VBase3, Vec4, Vec3
objectStruct = {
    'Objects': {
        '1302550960.6jubutler': {
            'Type': 'Ship Part',
            'Name': 'shipQueenAnne',
            'Category': "55: Queen Anne's Revenge",
            'File': '',
            'Flagship': False,
            'LogoOverride': '-1: Default',
            'Objects': {
                '1302551043.33jubutler': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'AuraFX': 'None',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(1.3999999999999999, -20.734000000000002, 25.053000000000001),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropFXLeft': 'None',
                    'PropFXRight': 'None',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'VoodooZombie T4',
                    'Start State': 'Patrol',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65000000000000002, 1),
                        'Model': 'models/misc/smiley' },
                    'spawnTimeBegin': 0.0,
                    'spawnTimeEnd': 0.0 },
                '1302551224.75jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(-11.023999999999999, -45.302, 24.596),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65000000000000002, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302551245.21jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': 100,
                    'Pause Duration': 30,
                    'Pos': Point3(7.6059999999999999, -45.433, 24.594000000000001),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65000000000000002, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302551263.39jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-10.083, 6.6239999999999997, 25.561),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65000000000000002, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302551267.54jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(10.468999999999999, 5.1929999999999996, 25.707000000000001),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65000000000000002, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1302561022.57jloehrle': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'AuraFX': 'None',
                    'Hpr': VBase3(-177.31299999999999, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-1.1499999999999999, 30.475999999999999, 27.427),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropFXLeft': 'None',
                    'PropFXRight': 'None',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'VoodooZombie T4',
                    'Start State': 'Patrol',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65000000000000002, 1),
                        'Model': 'models/misc/smiley' },
                    'spawnTimeBegin': 0.0,
                    'spawnTimeEnd': 0.0 } },
            'Respawns': True,
            'StyleOverride': '-1: Default',
            'Team': 'Player',
            'VisSize': '',
            'Visual': {
                'Model': [
                    'models/shipparts/interceptorL1-geometry_High',
                    'models/shipparts/interceptorL1-collisions'] } } },
    'Node Links': [
        [
            '1302551267.54jubutler',
            '1302551245.21jubutler',
            'Bi-directional'],
        [
            '1302551267.54jubutler',
            '1302551263.39jubutler',
            'Bi-directional'],
        [
            '1302551267.54jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302551245.21jubutler',
            '1302551224.75jubutler',
            'Bi-directional'],
        [
            '1302551245.21jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302551224.75jubutler',
            '1302551263.39jubutler',
            'Bi-directional'],
        [
            '1302551224.75jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302551263.39jubutler',
            '1302551043.33jubutler',
            'Bi-directional'],
        [
            '1302561022.57jloehrle',
            '1302551263.39jubutler',
            'Bi-directional'],
        [
            '1302561022.57jloehrle',
            '1302551267.54jubutler',
            'Bi-directional']],
    'Layers': { },
    'ObjectIds': {
        '1302550960.6jubutler': '["Objects"]["1302550960.6jubutler"]',
        '1302551043.33jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551043.33jubutler"]',
        '1302551224.75jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551224.75jubutler"]',
        '1302551245.21jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551245.21jubutler"]',
        '1302551263.39jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551263.39jubutler"]',
        '1302551267.54jubutler': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302551267.54jubutler"]',
        '1302561022.57jloehrle': '["Objects"]["1302550960.6jubutler"]["Objects"]["1302561022.57jloehrle"]' } }
extraInfo = {
    'camPos': Point3(-123.069, -59.1584, 128.28999999999999),
    'camHpr': VBase3(-67.752600000000001, -39.273499999999999, 0),
    'focalLength': 1.39951908588,
    'skyState': 2,
    'fog': 0 }
