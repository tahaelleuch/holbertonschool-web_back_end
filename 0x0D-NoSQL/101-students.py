#!/usr/bin/env python3
"""top students"""


def top_students(mongo_collection):
    """top students"""
    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students
