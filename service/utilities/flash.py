from flask import flash


def flash_form_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the {0} field - {1}".format(
                getattr(form, field).label.text,
                error
            ))
