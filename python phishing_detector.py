import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

class PhishingDetector:
    def __init__(self):
        
        self.vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, max_features=5000)
       
        self.model = MultinomialNB()

    def train(self, X_train, y_train):
        """Extracts features and trains the machine learning model."""
        print("[*] Extracting features using TF-IDF...")
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        
        print("[*] Training the Naive Bayes model...")
        self.model.fit(X_train_tfidf, y_train)
        print("[+] Model training completed successfully.")

    def evaluate(self, X_test, y_test):
        """Evaluates the model and displays Accuracy, Classification Report, and Confusion Matrix."""
        X_test_tfidf = self.vectorizer.transform(X_test)
        y_pred = self.model.predict(X_test_tfidf)

       
        accuracy = accuracy_score(y_test, y_pred)
        print("\n" + "="*20 + " MODEL EVALUATION " + "="*20)
        print(f"Overall Accuracy: {accuracy * 100:.2f}%")
        
       
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=["Safe", "Phishing"]))

       
        cm = confusion_matrix(y_test, y_pred)
        print("Confusion Matrix Data:")
        print(cm)
        
        
        self._plot_confusion_matrix(cm)

    def predict_raw_email(self, email_text):
        """Classifies a new, unseen single email text."""
        features = self.vectorizer.transform([email_text])
        prediction = self.model.predict(features)[0]
        return "Phishing" if prediction == 1 else "Safe"

    def _plot_confusion_matrix(self, cm):
        """Generates a visual popup graph of the confusion matrix."""
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Safe", "Phishing"])
        disp.plot(cmap=plt.cm.Blues)
        plt.title("Phishing Detection - Confusion Matrix")
        print("\n[INFO] Close the confusion matrix plot window to finish script execution.")
        plt.show()


if __name__ == "__main__":
   
    mock_emails = [
        "Hey, are we still meeting for lunch today at 1 PM? Let me know.",
        "URGENT: Your bank account has been compromised! Click here immediately to reset your password: http://fake-login-bank.com",
        "The project report is attached. Please review it before the deadline tomorrow.",
        "Dear customer, you won a $1000 Walmart gift card! Verify your SSN and claim your prize now at http://win-free-rewards.xyz",
        "Can you send me the updated API documentation? Thanks, John.",
        "Official Netflix Notice: Update your payment details within 24 hours or your subscription will be suspended! http://netflix-verify-user.net",
        "Hi Mom, I forgot my jacket at your house. I will pick it up this weekend.",
        "Your package from Amazon could not be delivered. Update your billing address now to avoid return fees: http://track-parcel-now.info"
    ]
    
    
    mock_labels = [0, 1, 0, 1, 0, 1, 0, 1]  

   
    X = mock_emails * 5
    y = mock_labels * 5

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  
    detector = PhishingDetector()
    detector.train(X_train, y_train)
    detector.evaluate(X_test, y_test)

   
    print("\n" + "-"*20 + " LIVE INFERENCE TEST " + "-"*20)
    sample_email = "🚨 SECURITY ALERT: Someone accessed your account from Russia. Click this link to secure your funds now!"
    result = detector.predict_raw_email(sample_email)
    print(f"Sample Email: \"{sample_email}\"")
    print(f"Model Classification Result: ---> {result} <---")