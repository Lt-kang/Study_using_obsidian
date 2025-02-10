from pathlib import Path


def create_md_file(dir: Path):
    dir_name = dir.name
    f = open(f'{dir / dir_name}.md', 'w', encoding='utf-8-sig')

    for md_file in dir.glob('*.md'):
        if md_file.stem == dir_name: continue
        f.write(f'[[{md_file.stem}]]  \n')

    f.close()


def create_md_file_with_file(dir: Path):
    dir_name = dir.name
    f = open(f'{dir / dir_name}.md', 'w', encoding='utf-8-sig')

    for normal_dir in dir.glob('*'):
        if normal_dir.stem == dir_name: continue
        if normal_dir.is_file(): continue

        f.write(f'[[{normal_dir.stem}]]  \n')

    f.close()



def create_guide_md(dir: Path):
    for _dir in dir.iterdir():
        if _dir.is_dir():
            if list(_dir.glob('*')) == list(_dir.glob('*.md')): # md파일 밖에 없는 최종 트리
                create_md_file(_dir)

            elif [d for d in _dir.glob('*') if '.md' != d.suffix] != []: # 폴더 뿐인 경우 상위 폴더에 연결
                create_md_file_with_file(_dir)

            else:
                create_guide_md(_dir)




if __name__ == '__main__':
    base_path = Path(__file__).parent

    for dir in ['Web', 'Statistics', 'Python', 'Ai', 'Math', 'ETC']:
        create_guide_md(base_path / dir)

    # for dir in base_path.iterdir():
    #     if dir.is_file():
    #         continue

    #     if dir.is_dir():
    #         ...
    


    print('done')