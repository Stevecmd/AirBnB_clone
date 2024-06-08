#!/usr/bin/python3
"""
Defines a base model class.

    This class defines all common attributes/methods for other classes.
"""
# Imports
from datetime import datetime
from uuid import uuid4
from collections import OrderedDict
import models


class BaseModel:
    """Represents the "base" for all other classes."""

    # kwargs is a dictionary
    def __init__(self, *args, **kwargs):
        """
        Initialize.

        Initializes a new BaseModel/ Instance

        Args:
            id (int): Unique id for each BaseModel
            created_at: Date of object creation
            updated_at: Date of object change
        """
        # tform = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            # Create from dictionary, Loop dictionary key and values
            for key, value in kwargs.items():
                # Set object attributes dynamically using setattr function
                if (key == "__class__"):
                    continue

                # Convert isoformat string date to datetime object
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """
        Update.

        Update on the public instance attribute.

        Updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return an OrderedDict.

        OrderedDict contains all keys/values of __dict__ of
        the instance in the desired order.
        """
        ordered_dict = OrderedDict()
        if hasattr(self, 'my_number'):
            ordered_dict["my_number"] = self.my_number
        if hasattr(self, 'name'):
            ordered_dict["name"] = self.name
        ordered_dict["__class__"] = self.__class__.__name__
        ordered_dict["updated_at"] = self.updated_at.isoformat()
        ordered_dict["id"] = self.id
        ordered_dict["created_at"] = self.created_at.isoformat()

        # Return as a regular dictionary
        return dict(ordered_dict)

    def __str__(self):
        """Return the printable representation of model."""
        return "[{}] ({}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)
