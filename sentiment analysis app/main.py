import streamlit as st
import spacy_streamlit
import spacy
import pickle
from google_trans_new import google_translator


def load_model():
	model = pickle.load('log_reg.pkl')
	tf_idf = pickle.load('tf_idf.pkl')

def main():
	"""
	A simple NLP app
	"""
	# model = pickle.load(open('log_reg.pkl'))
	# tf_idf = pickle.load(open('tf_idf.pkl'))

	with open('pickle files/log_reg.pkl', 'rb') as f:
		model = pickle.load(f)
		
	with open('pickle files/tf_idf.pkl', 'rb') as f:
		tf_idf = pickle.load(f)
		
	st.title('Olist User Review')
	menu = ['Home', 'About']
	choice = st.sidebar.selectbox('Menu', menu)

	if choice == 'Home':
		st.subheader('Sentiment Analysis')
		review = st.text_area('Review Text', 'Enter your Reviews')

		translator = google_translator()
		trans_text = translator.translate(text=review, lang_tgt='en')
		st.write('Would you like to translate')
		if st.button('Translate'):
			st.text_area('Translated Review Text', trans_text)
		if st.button('Get Sentiment'):
			prediction = int(model.predict(tf_idf.transform([review])))
			if prediction == 1:
				st.success('**Review text is Positive :joy: :yum:**')
			elif prediction == -1:
				st.error('**Review text is Negative :cry: :worried:**')


	if choice == 'About':
		st.subheader('Learn More About Sentiment Analysis')
		st.write('## Model was built using Logistic Regression :sunglasses:')




if __name__ == '__main__':
	main()