# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateReferenceDetails(object):
    """
    Application references that need to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateReferenceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param options:
            The value to assign to the options property of this UpdateReferenceDetails.
        :type options: dict(str, str)

        :param target_object:
            The value to assign to the target_object property of this UpdateReferenceDetails.
        :type target_object: object

        :param child_references:
            The value to assign to the child_references property of this UpdateReferenceDetails.
        :type child_references: list[ChildReferenceDetail]

        """
        self.swagger_types = {
            'options': 'dict(str, str)',
            'target_object': 'object',
            'child_references': 'list[ChildReferenceDetail]'
        }

        self.attribute_map = {
            'options': 'options',
            'target_object': 'targetObject',
            'child_references': 'childReferences'
        }

        self._options = None
        self._target_object = None
        self._child_references = None

    @property
    def options(self):
        """
        Gets the options of this UpdateReferenceDetails.
        A list of options such as `ignoreObjectOnError`.


        :return: The options of this UpdateReferenceDetails.
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this UpdateReferenceDetails.
        A list of options such as `ignoreObjectOnError`.


        :param options: The options of this UpdateReferenceDetails.
        :type: dict(str, str)
        """
        self._options = options

    @property
    def target_object(self):
        """
        Gets the target_object of this UpdateReferenceDetails.
        The new target object to reference. This should be of type `DataAsset`. The child references can be of type `Connection`.


        :return: The target_object of this UpdateReferenceDetails.
        :rtype: object
        """
        return self._target_object

    @target_object.setter
    def target_object(self, target_object):
        """
        Sets the target_object of this UpdateReferenceDetails.
        The new target object to reference. This should be of type `DataAsset`. The child references can be of type `Connection`.


        :param target_object: The target_object of this UpdateReferenceDetails.
        :type: object
        """
        self._target_object = target_object

    @property
    def child_references(self):
        """
        Gets the child_references of this UpdateReferenceDetails.
        The list of child references that also need to be updated.


        :return: The child_references of this UpdateReferenceDetails.
        :rtype: list[ChildReferenceDetail]
        """
        return self._child_references

    @child_references.setter
    def child_references(self, child_references):
        """
        Sets the child_references of this UpdateReferenceDetails.
        The list of child references that also need to be updated.


        :param child_references: The child_references of this UpdateReferenceDetails.
        :type: list[ChildReferenceDetail]
        """
        self._child_references = child_references

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
