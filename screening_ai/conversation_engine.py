class ConversationStateMachine:

    def __init__(self, flow):

        self.flow = flow["nodes"]
        self.current_node = flow["start"]
        self.retry_count = {}

    def get_question(self):

        if self.current_node == "END":
            return None

        return self.flow[self.current_node]["question"]

    def next(self):

        if self.current_node == "END":
            return

        self.current_node = self.flow[self.current_node].get(
            "next",
            "END"
        )

    def handle_silence(self):

        node = self.flow[self.current_node]

        retry_node = node.get("on_silence")

        if retry_node:

            self.retry_count.setdefault(
                self.current_node,
                0
            )

            self.retry_count[self.current_node] += 1

            max_retries = node.get(
                "max_retries",
                2
            )

            if self.retry_count[self.current_node] <= max_retries:

                self.current_node = retry_node

            else:

                self.current_node = "END"

    def handle_confusion(self):

        node = self.flow[self.current_node]

        if "on_confusion" in node:

            self.current_node = node["on_confusion"]

    def handle_repeat(self):

        node = self.flow[self.current_node]

        if "on_repeat" in node:

            self.current_node = node["on_repeat"]

    def is_end(self):

        return self.current_node == "END"