#!/usr/bin/env -S uv run python3
# asyncio示例

import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


if __name__ == "__main__":
    asyncio.run(main())
