from flask_wtf import FlaskForm
from wtforms.fields import DecimalField,SubmitField
from wtforms.validators import DataRequired


class details(FlaskForm):
    crim=DecimalField('CRIM',validators=[DataRequired()])
    zn=DecimalField('ZN',validators=[DataRequired()])
    indus=DecimalField('INDUS',validators=[DataRequired()])
    chas=DecimalField('CHAS',validators=[DataRequired()])
    nox=DecimalField('NOX',validators=[DataRequired()])
    rm=DecimalField('RM',validators=[DataRequired()])
    age=DecimalField('AGE',validators=[DataRequired()])
    dis=DecimalField('DIS',validators=[DataRequired()])
    rad=DecimalField('RAD',validators=[DataRequired()])
    tax=DecimalField('TAX',validators=[DataRequired()])
    ptratio=DecimalField('PTRATIO',validators=[DataRequired()])
    b=DecimalField('B',validators=[DataRequired()])
    lstat=DecimalField('LSTAT',validators=[DataRequired()])
    submit=SubmitField('Predict House Price')
