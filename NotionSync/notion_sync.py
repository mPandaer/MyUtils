from notion_client import Client
import settings
import os

# notion = Client(auth=settings.TOKEN)
#
# notion.pages.create(**{
#     "parent": {"database_id": settings.DATABASE_ID},
#     "properties": {
#         "title": {
#             "title": [
#                 {
#                     "text": {
#                         "content": "MAC OS 提交"
#                     }
#                 }
#             ]
#         }
#     },
# })

if __name__ == '__main__':
    os.system("brew doctor")
