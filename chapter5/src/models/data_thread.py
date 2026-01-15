from pydantic import BaseModel, Field


class DataThread(BaseModel):
    """生成されたコードとその実行結果を保持するためのデータ型"""

    process_id: str
    thread_id: int
    user_request: str | None
    code: str | None = None
    error: str | None = None
    stderr: str | None = None
    stdout: str | None = None
    is_completed: bool = False
    observation: str | None = None
    results: list[dict] = Field(default_factory=list)
    pathes: dict = Field(default_factory=dict)
