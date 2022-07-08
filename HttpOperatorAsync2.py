from airflow.providers.http.operators.http import SimpleHttpOperator



class HttpOperatorAsync(SimpleHttpOperator):

    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello"
        self.defer(trigger=HttpTrigger(
            method="GET", 
            http_conn_id='api_posts',
            endpoint="posts/"
        ),method_name="execute_complete")
        print(message)
        return message

    def execute_complete(self, context, event):
        message = f"Hello Trigger Pulled"
        print(message)
        return message
    
        

