import json
import os
from datetime import datetime

class QueueManager:
    def __init__(self, queue_file='queue.json'):
        self.queue_file = queue_file
        self.queue = self.load_queue()

    def load_queue(self):
        """Load queue from file"""
        if os.path.exists(self.queue_file):
            with open(self.queue_file, 'r') as f:
                return json.load(f)
        return []

    def save_queue(self):
        """Save queue to file"""
        with open(self.queue_file, 'w') as f:
            json.dump(self.queue, f, indent=2)

    def add_to_queue(self, item):
        """Add item to queue"""
        item['timestamp'] = datetime.now().isoformat()
        item['status'] = 'pending'
        self.queue.append(item)
        self.save_queue()

    def get_pending_items(self):
        """Get all pending items"""
        return [item for item in self.queue if item['status'] == 'pending']

    def mark_completed(self, item_id):
        """Mark item as completed"""
        for item in self.queue:
            if item.get('id') == item_id:
                item['status'] = 'completed'
                self.save_queue()
                break

    def reprocess_queue(self):
        """Reprocess pending items (stub)"""
        pending = self.get_pending_items()
        for item in pending:
            # Simulate reprocessing
            print(f"Reprocessing: {item}")
            # In real implementation, call engine or something
            self.mark_completed(item.get('id', 'unknown'))