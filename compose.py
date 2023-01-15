import os
import datetime 
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('title',type=str)
    parser.add_argument('--categories',type=str,required=False,default='')
    parser.add_argument('--tags',type=str,required=False,default='')
    args = parser.parse_args()

    fn = datetime.datetime.now().strftime("%Y-%m-%d") + '-' \
            + args.title.replace(' ','') + '.md'

    content = '---\n' + \
            'title: {}\n'.format(args.title) + \
            'date: {}\n'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S +0800")) + \
            'categories: [{}]\n'.format(args.categories)  + \
            'tags: [{}]\n'.format(args.tags) + \
            '---\n'
    with open('_posts/{}'.format(fn),'w') as f:
        f.write(content)