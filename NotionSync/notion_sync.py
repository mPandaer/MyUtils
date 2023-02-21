from notion_client import Client
import os

# Initialize the client
# 取得token的方法，可以參考官方文件這邊 https://developers.notion.com/docs/getting-started
NOTION_TOKEN = ""
DATABASE_ID = ""
notion = Client(auth=NOTION_TOKEN)


def insert_to_notion(date: str, content: str, title="Work note", tag="work"):
    # 這邊需要`DATABASE_ID`，可以在網頁版Notion點選page後，網址最後會有一個id，可以在這邊抓取
    # 例如 https://www.notion.so/natlee/test-4f3f55661c333e5585660c4c35e10533
    # 這邊的DATABASE_ID就是`4f3f55661c333e5585660c4c35e10533`

    notion.pages.create(
        **{
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "title": {"title": [{"type": "text", "text": {"content": title}}]},  # 標題的屬性跟標題是什麼
                "Tags": {"type": "multi_select", "multi_select": [{"name": tag}]},  # 標籤的屬性跟標籤是什麼
            },
            "children": [  # 這邊比較麻煩，要指定內容是哪種屬性，例如paragraph
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": content}}]  # 內文的屬性跟內容
                    },
                }
            ],
        }
    )


if __name__ == '__main__':
    insert_to_notion('2022-10-10', "# 测试")
